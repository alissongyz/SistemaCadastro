# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_OXIPARTS(object):
    def setupUi(self, OXIPARTS):
        if not OXIPARTS.objectName():
            OXIPARTS.setObjectName(u"OXIPARTS")
        OXIPARTS.resize(462, 471)
        font = QFont()
        font.setFamily(u"Arial")
        font.setBold(False)
        font.setWeight(50)
        OXIPARTS.setFont(font)
        icon = QIcon()
        icon.addFile(u"tentativa1000/logoSystem.png", QSize(), QIcon.Normal, QIcon.Off)
        OXIPARTS.setWindowIcon(icon)
        OXIPARTS.setStyleSheet(u"background-color: rgb(222, 209, 28);\n"
"background-color: rgb(212, 0, 3);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(OXIPARTS)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 251, 41))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 130, 131, 16))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 180, 171, 16))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_4.setFont(font3)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 130, 231, 20))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(170, 180, 251, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(190, 230, 231, 21))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 280, 181, 16))
        self.label_5.setFont(font3)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 230, 131, 21))
        self.label_6.setFont(font3)
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(230, 280, 191, 21))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 380, 101, 31))
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 420, 151, 31))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 174, 10);")
        OXIPARTS.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(OXIPARTS)
        self.statusbar.setObjectName(u"statusbar")
        OXIPARTS.setStatusBar(self.statusbar)

        self.retranslateUi(OXIPARTS)

        QMetaObject.connectSlotsByName(OXIPARTS)
    # setupUi

    def retranslateUi(self, OXIPARTS):
        OXIPARTS.setWindowTitle(QCoreApplication.translate("OXIPARTS", u"OXIPARTS - Cadastro de Pe\u00e7as", None))
        self.label.setText(QCoreApplication.translate("OXIPARTS", u"Cadastro de Clientes", None))
        self.label_2.setText(QCoreApplication.translate("OXIPARTS", u"Nome do Cliente:", None))
        self.label_4.setText(QCoreApplication.translate("OXIPARTS", u"Nome da Pe\u00e7a:", None))
        self.label_5.setText(QCoreApplication.translate("OXIPARTS", u"Quantidade do Pedido:", None))
        self.label_6.setText(QCoreApplication.translate("OXIPARTS", u"Data de Entrega:", None))
        self.pushButton.setText(QCoreApplication.translate("OXIPARTS", u"Cadastrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("OXIPARTS", u"Acessar Cadastros", None))
    # retranslateUi

