from .styles import highlightComboBox, highlightLineEdit, resetComboBoxHighlight, resetLineEditHighlight
from .constants import *
from .gui.DlgQuestionnaire import Ui_DlgQuestionnaire

from qgis.PyQt.QtCore import QSettings,QUrl, Qt
from qgis.PyQt import QtWidgets, QtCore
from qgis.PyQt.QtGui import QDesktopServices
from . import log
import requests
settings = QSettings()

class DlgQuestionnaire(QtWidgets.QDialog, Ui_DlgQuestionnaire):
    def __init__(self, parent=None):
        super(DlgQuestionnaire, self).__init__(parent)

        self.setupUi(self)

        # self.dlg_settings_register = DlgQuestionnaireRegister()
       
        # self.dlg_settings_edit = DlgQuestionnaireEdit()
        self.filePushButton.clicked.connect(self.fetchFile)
        self.createPushButton.clicked.connect(self.create)
    
    def fetchFile(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Excel File", "", "Excel Files (*.xlsx *.xls)")
        if file_path:
            self.fileLineEdit.setText(file_path)
        
    def create(self):
        log("Creating questionnaire")

        if not self.projectLineEdit.text():
            highlightLineEdit(self.titleLineEdit)
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide a project name"))
            return

        if not self.titleLineEdit.text():
            highlightLineEdit(self.titleLineEdit)
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide a title"))
            return
        
        if not self.descriptionTextEdit.toPlainText():
            highlightLineEdit(self.descriptionTextEdit)
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide a brief description"))
            return
        
        if not self.fileLineEdit.text():
            highlightLineEdit(self.fileLineEdit)
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide an excel file"))
            return
        token = QtCore.QSettings().value("WAJIR_ICGS/token",None)
        log(f"User token:{token}")
        if token is None:
            QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS","Please login to proceed"))
            return
        
        progress_dialog = QtWidgets.QProgressDialog("Processing...", "Cancel", 0, 100, self)
        progress_dialog.setWindowTitle("Creating questionnaire")
        progress_dialog.setWindowModality(Qt.WindowModal)

        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)

        progress_dialog.show()
        QtWidgets.QApplication.processEvents()
        headers = {
            "Authorization": f"Bearer {token}",  # Replace with actual token
            "Accept": "application/json"
        }
        
        files = {'excel_file': open(self.fileLineEdit.text(), 'rb')}
        payload = {
            'title':self.titleLineEdit.text(),
            'name':self.projectLineEdit.text(),
            'description': self.descriptionTextEdit.toPlainText(),
        }
        progress_dialog.setLabelText("Creating questionnaire...")
        progress_bar.setValue(50)
        response = requests.post(f"{baseURL}/api/data_handler/excel_upload/", data=payload, files=files, headers=headers)

        if response.status_code == 201:
            progress_bar.setValue(100)
            progress_dialog.close()
            log("Questionnaire created successfully")
            QtWidgets.QMessageBox.information(None,
                QtWidgets.QApplication.translate("WAJIR_ICGS", "Success"),
                QtWidgets.QApplication.translate("WAJIR_ICGS", "File uploaded successfully!"))
            self.close()

        elif response.status_code == 401:
            log("Session expired. Error code: {}".format(response.status_code))
            QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("Session expired. Error code: {}".format(response.status_code)))
        elif response.json().get("excel_file") is not None:
            log(f"{response.json().get("excel_file")[0]['options']}. Error code: {response.status_code}")
            QtWidgets.QMessageBox.critical (None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS",f"{response.json().get("excel_file")[0]['options']}. Error code: {response.status_code}"))
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
        