# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DlgSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DlgSettings(object):
    def setupUi(self, DlgSettings):
        DlgSettings.setObjectName("DlgSettings")
        DlgSettings.resize(369, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DlgSettings.sizePolicy().hasHeightForWidth())
        DlgSettings.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(DlgSettings)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(DlgSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.emailLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLineEdit.sizePolicy().hasHeightForWidth())
        self.emailLineEdit.setSizePolicy(sizePolicy)
        self.emailLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.emailLineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.emailLineEdit.setFont(font)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.verticalLayout_2.addWidget(self.emailLineEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordLineEdit.sizePolicy().hasHeightForWidth())
        self.passwordLineEdit.setSizePolicy(sizePolicy)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.passwordLineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.verticalLayout_2.addWidget(self.passwordLineEdit)
        self.loginPushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginPushButton.sizePolicy().hasHeightForWidth())
        self.loginPushButton.setSizePolicy(sizePolicy)
        self.loginPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.loginPushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.loginPushButton.setFont(font)
        self.loginPushButton.setObjectName("loginPushButton")
        self.verticalLayout_2.addWidget(self.loginPushButton)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(DlgSettings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setContentsMargins(-1, 12, -1, 12)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signUpPushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signUpPushButton.sizePolicy().hasHeightForWidth())
        self.signUpPushButton.setSizePolicy(sizePolicy)
        self.signUpPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.signUpPushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.signUpPushButton.setFont(font)
        self.signUpPushButton.setObjectName("signUpPushButton")
        self.verticalLayout.addWidget(self.signUpPushButton)
        self.forgotPasswordPushButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forgotPasswordPushButton.sizePolicy().hasHeightForWidth())
        self.forgotPasswordPushButton.setSizePolicy(sizePolicy)
        self.forgotPasswordPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.forgotPasswordPushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.forgotPasswordPushButton.setFont(font)
        self.forgotPasswordPushButton.setObjectName("forgotPasswordPushButton")
        self.verticalLayout.addWidget(self.forgotPasswordPushButton)
        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.retranslateUi(DlgSettings)
        QtCore.QMetaObject.connectSlotsByName(DlgSettings)

    def retranslateUi(self, DlgSettings):
        _translate = QtCore.QCoreApplication.translate
        DlgSettings.setWindowTitle(_translate("DlgSettings", "Settings"))
        self.groupBox.setTitle(_translate("DlgSettings", "Login"))
        self.label_3.setText(_translate("DlgSettings", "Welcome"))
        self.label_4.setText(_translate("DlgSettings", "Fill in your credentials similar to the one on the data collection application"))
        self.label.setText(_translate("DlgSettings", "Email:"))
        self.label_2.setText(_translate("DlgSettings", "Password:"))
        self.loginPushButton.setText(_translate("DlgSettings", "Login"))
        self.groupBox_2.setTitle(_translate("DlgSettings", "Create/Retrieve Account"))
        self.signUpPushButton.setText(_translate("DlgSettings", "Sign up"))
        self.forgotPasswordPushButton.setText(_translate("DlgSettings", "Forgot Password"))
