from .styles import highlightComboBox, highlightLineEdit, resetComboBoxHighlight, resetLineEditHighlight
from .gui.DlgShare import Ui_DlgShare
from .gui.DlgQuestionnaireDetails import Ui_DlgQuestionnaireDetails

from qgis.PyQt.QtCore import QSettings,QUrl, Qt
from qgis.PyQt import QtWidgets, QtCore
from qgis.PyQt.QtGui import QDesktopServices, QPixmap
from qgis.PyQt.QtNetwork import QNetworkAccessManager, QNetworkRequest
from qgis.core import QgsVectorLayer, QgsProject
import requests
from .constants import *
from . import log
settings = QSettings()

class DlgShare(QtWidgets.QDialog, Ui_DlgShare):
    def __init__(self, parent=None):
        super(DlgShare, self).__init__(parent)

        self.setupUi(self)
        self.data_loaded = False

        self.questionnaireComboBox.currentIndexChanged.connect(self.on_selection_changed)
        self.refreshPushButton.clicked.connect(self.fetchQuestionniares)
        self.sharePushButton.clicked.connect(self.share)
    
    def showEvent(self, event):
        """Triggered when the dialog is shown."""
        super().showEvent(event)
        if not self.data_loaded:
            self.fetchQuestionniares()
            self.data_loaded = True

    def on_selection_changed(self):
        log(str(self.questionnaireComboBox.currentData()))
    
    def get_file_path(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Select Output File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_path:
            self.outputLineEdit.setText(file_path)

    def fetchQuestionniares(self):
        progress_dialog = QtWidgets.QProgressDialog("Processing...", "Cancel", 0, 100, self)
        progress_dialog.setWindowTitle("Fetching Questionnaires")
        progress_dialog.setWindowModality(Qt.WindowModal)

        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)

        progress_dialog.show()
        QtWidgets.QApplication.processEvents()
        log("Fetching questionniares")
        token = QtCore.QSettings().value("WAJIR_ICGS/token",None)
        log(f"User token:{token}")
        if token is None:
            QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS","Please login to proceed"))
            return
        progress_dialog.setLabelText("Fetching Questionnaires...")
        progress_bar.setValue(10)
        headers = {
            "Authorization": f"Bearer {token}",
        }
        response = requests.get(f"{baseURL}/api/data_handler/questionnaires/", headers=headers)
        log(str(response.status_code))
        log(str(response.json()))
        progress_bar.setValue(40)
        if response.status_code == 200:
            questionnaires = response.json().get("results")
            progress_bar.setValue(90)
            log(str(questionnaires))
            if(len(questionnaires) == 0):
                log("User has no questionnaires")
                QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS","You have not created any questionnaires."))
                return

            self.questionnaireComboBox.clear()  # Clear existing items

            for questionnaire in questionnaires:
                self.questionnaireComboBox.addItem(questionnaire["title"], (questionnaire["qr_code"], questionnaire['id']))  # Display title, store ID

            # Optional: Set the first item as default
            if self.questionnaireComboBox.count() > 0:
                self.questionnaireComboBox.setCurrentIndex(0)
            progress_bar.setValue(100)
            progress_dialog.close()
        elif response.status_code == 401:
            log("Session expired.  Please login again to proceed. Error code: {}".format(response.status_code))
            QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS","Session expired. Please login again to proceed. Error code: {}".format(response.status_code)))
        elif str(response.status_code).startswith("5"):
            log("Could not connect to the WAJIR_ICGS server due to a server error. Error code: {}".format(response.status_code))
            QtWidgets.QMessageBox.critical(None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Could not connect to the WAJIR_ICGS server due to a server error. Error code: {}".format(response.status_code)))
        else:
            log("Could not connect to the WAJIR_ICGS server. Error code: {}".format(response.status_code))
            log(str(response.json()))
            QtWidgets.QMessageBox.critical(None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Could not connect to the WAJIR_ICGS. Error code: {}".format(response.status_code)))
    
    def share(self):
        self.close()
        qr_code, questionnaire_id = self.questionnaireComboBox.currentData()
        link = f"{baseURL}/api/data_handler/questionnaires/{questionnaire_id}"
        dialog = DlgQuestionnaireDetails(qr_code, link)
        dialog.exec_()

class DlgQuestionnaireDetails(QtWidgets.QDialog, Ui_DlgQuestionnaireDetails):
    def __init__(self, image_path, link, parent=None):
        super(DlgQuestionnaireDetails, self).__init__(parent)

        self.setupUi(self)
        self.linkLabel.setText(f'<a href="{link}">{link}</a>')

        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self.on_image_downloaded)

        # Start downloading the image
        self.manager.get(QNetworkRequest(QUrl(image_path)))

    def on_image_downloaded(self, reply):
        if reply.error():
            print(f"Error downloading image: {reply.errorString()}")
            return

        # Read the image data and load it into a QPixmap
        image_data = reply.readAll()
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        # Set the downloaded image into the QLabel
        self.qrLabel.setPixmap(pixmap)
        self.qrLabel.setScaledContents(True) 