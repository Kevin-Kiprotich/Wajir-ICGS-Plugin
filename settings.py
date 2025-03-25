from .styles import highlightComboBox, highlightLineEdit, resetComboBoxHighlight, resetLineEditHighlight
from .gui.DlgSettings import Ui_DlgSettings

from qgis.PyQt.QtCore import QSettings,QUrl,Qt
from qgis.PyQt import QtWidgets, QtCore
from qgis.PyQt.QtGui import QDesktopServices
import requests
from .constants import *
from . import log
settings = QSettings()

class DlgSettings(QtWidgets.QDialog, Ui_DlgSettings):
    def __init__(self, parent=None):
        super(DlgSettings, self).__init__(parent)

        self.setupUi(self)

        # self.dlg_settings_register = DlgSettingsRegister()
       
        # self.dlg_settings_edit = DlgSettingsEdit()

        self.signUpPushButton.clicked.connect(self.register)
        self.loginPushButton.clicked.connect(self.login)
        self.forgotPasswordPushButton.clicked.connect(self.forgot_pwd)

    # """
    #     This is modified to connect to the MISLAND platform for unified registration    
    # """
    def register(self):
        url = QUrl('http://misland-africa.oss-online.org/#/register') #This holds the url for registration of new users in the QGIS plugin
        QDesktopServices.openUrl(url)
    #     result = self.dlg_settings_register.exec_()

    def login(self):
        print(self.emailLineEdit.text())
        print(self.passwordLineEdit.text())

        if not self.emailLineEdit.text():
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide an email"))
            return
        
        if not self.passwordLineEdit.text():
            highlightComboBox(self.CountryComboBox)
            QtWidgets.QMessageBox.critical(None, self.tr("Error"),
                                       self.tr("Please provide a password"))
            return

        progress_dialog = QtWidgets.QProgressDialog("Processing...", "Cancel", 0, 100, self)
        progress_dialog.setWindowTitle("Login")
        progress_dialog.setWindowModality(Qt.WindowModal)

        progress_bar = QtWidgets.QProgressBar(progress_dialog)
        progress_dialog.setBar(progress_bar)

        progress_dialog.show()
        QtWidgets.QApplication.processEvents()
        payload = {
            'email':self.emailLineEdit.text(),
            'password':self.passwordLineEdit.text()
        }
        progress_dialog.setLabelText("Loging in ...")
        progress_bar.setValue(50)
        response = requests.post(f"{baseURL}/api/accounts/login/",json=payload)

        if response.status_code == 200:
            progress_bar.setValue(100)
            progress_dialog.close()
            log("Login successful")
            QtCore.QSettings().setValue("WAJIR_ICGS/token", response.json().get("access"))
            QtWidgets.QMessageBox.information(None,
                QtWidgets.QApplication.translate("WAJIR_ICGS", "Success"),
                QtWidgets.QApplication.translate("WAJIR_ICGS", "Login successful!"))
            self.close()
        elif str(response.status_code).startswith("5"):
            log("Could not connect to the WAJIR_ICGS server due to a server error. Error code: {}".format(response.status_code))
            QtWidgets.QMessageBox.critical(None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Could not connect to the WAJIR_ICGS server due to a server error. Error code: {}".format(response.status_code)))
            return None
        elif response.json().get("login") is not None:
            log(f"{response.json().get("login")[0]}. Error code: {response.status_code}")
            QtWidgets.QMessageBox.critical(None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", response.json().get("login")[0]))
            return None
        else:
            log("Could not connect to the WAJIR_ICGS server. Error code: {}".format(response.status_code))
            QtWidgets.QMessageBox.critical(None,
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Error"),
                                    QtWidgets.QApplication.translate("WAJIR_ICGS", "Could not connect to the WAJIR_ICGS. Error code: {}".format(response.status_code)))



        # result = self.dlg_settings_login.exec_()
        # if result and self.dlg_settings_login.ok:
        #     self.close()

    # def edit(self):
    #     if not get_user_email():
    #         # Note that the get_user_email will display a message box warning 
    #         # the user to register.
    #         return

    #     self.dlg_settings_edit.exec_()

    def forgot_pwd(self):
        url=QUrl('http://misland-africa.oss-online.org/#/forgot-password')
        QDesktopServices.openUrl(url)