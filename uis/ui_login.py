# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\projects\mypyqt\uis/login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        LoginWidget.setObjectName("LoginWidget")
        LoginWidget.resize(394, 263)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(LoginWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditPWD = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPWD.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditPWD.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEditPWD.setObjectName("lineEditPWD")
        self.gridLayout.addWidget(self.lineEditPWD, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEditUser = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditUser.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEditUser.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEditUser.setObjectName("lineEditUser")
        self.gridLayout.addWidget(self.lineEditUser, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(LoginWidget)
        self.pushButtonLogin.setMinimumSize(QtCore.QSize(184, 50))
        self.pushButtonLogin.setMaximumSize(QtCore.QSize(184, 50))
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonCancel = QtWidgets.QPushButton(LoginWidget)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(184, 50))
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(184, 50))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LoginWidget)
        QtCore.QMetaObject.connectSlotsByName(LoginWidget)

    def retranslateUi(self, LoginWidget):
        _translate = QtCore.QCoreApplication.translate
        LoginWidget.setWindowTitle(_translate("LoginWidget", "Form"))
        self.groupBox.setTitle(_translate("LoginWidget", "登录"))
        self.label.setText(_translate("LoginWidget", "密码"))
        self.label_2.setText(_translate("LoginWidget", "用户"))
        self.pushButtonLogin.setText(_translate("LoginWidget", "登录"))
        self.pushButtonCancel.setText(_translate("LoginWidget", "取消"))

