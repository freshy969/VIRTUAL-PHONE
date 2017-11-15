# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonebook.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 665)
        Dialog.setMinimumSize(QtCore.QSize(1123, 665))
        Dialog.setMaximumSize(QtCore.QSize(1123, 665))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("phonebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(161, 191, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 1061, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_contacts = QtWidgets.QWidget()
        self.tab_contacts.setObjectName("tab_contacts")
        self.btn_add_contact = QtWidgets.QPushButton(self.tab_contacts)
        self.btn_add_contact.setGeometry(QtCore.QRect(820, 210, 161, 51))
        self.btn_add_contact.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);\n"
"\n"
"")
        self.btn_add_contact.setObjectName("btn_add_contact")
        self.btn_backup = QtWidgets.QPushButton(self.tab_contacts)
        self.btn_backup.setGeometry(QtCore.QRect(820, 300, 161, 51))
        self.btn_backup.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_backup.setObjectName("btn_backup")
        self.table_contacts = QtWidgets.QTableWidget(self.tab_contacts)
        self.table_contacts.setGeometry(QtCore.QRect(20, 40, 731, 471))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.table_contacts.setFont(font)
        self.table_contacts.setStyleSheet("background-color: rgb(238, 238, 238);\n"
"font: 75 10pt \"Arial\";")
        self.table_contacts.setRowCount(10)
        self.table_contacts.setColumnCount(5)
        self.table_contacts.setObjectName("table_contacts")
        self.table_contacts.horizontalHeader().setDefaultSectionSize(150)
        self.table_contacts.horizontalHeader().setStretchLastSection(True)
        self.table_contacts.verticalHeader().setVisible(False)
        self.table_contacts.verticalHeader().setDefaultSectionSize(42)
        self.table_contacts.verticalHeader().setStretchLastSection(False)
        self.table_contacts.verticalHeader().setMinimumSectionSize(40)
        self.tabWidget.addTab(self.tab_contacts, "")
        self.tab_voicemsg = QtWidgets.QWidget()
        self.tab_voicemsg.setStyleSheet("font: 75 15pt \"Comic Sans MS\";")
        self.tab_voicemsg.setObjectName("tab_voicemsg")
        self.list_vmsg_contacts = QtWidgets.QListWidget(self.tab_voicemsg)
        self.list_vmsg_contacts.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.list_vmsg_contacts.setStyleSheet("background-color: rgb(238, 238, 238);""font: 75 16pt \"Consolas\";")
        self.list_vmsg_contacts.setObjectName("list_vmsg_contacts")
        self.list_vmsg_audios = QtWidgets.QListWidget(self.tab_voicemsg)
        self.list_vmsg_audios.setGeometry(QtCore.QRect(430, 40, 371, 471))
        self.list_vmsg_audios.setStyleSheet("background-color: rgb(238, 238, 238);""font: 75 16pt \"Consolas\";")
        self.list_vmsg_audios.setObjectName("list_vmsg_audios")
        self.btn_send_vmsg = QtWidgets.QPushButton(self.tab_voicemsg)
        self.btn_send_vmsg.setGeometry(QtCore.QRect(830, 230, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_send_vmsg.setFont(font)
        self.btn_send_vmsg.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_send_vmsg.setObjectName("btn_send_vmsg")
        self.tabWidget.addTab(self.tab_voicemsg, "")
        self.tab_sms = QtWidgets.QWidget()
        self.tab_sms.setObjectName("tab_sms")
        self.list_sms_contacts = QtWidgets.QListWidget(self.tab_sms)
        self.list_sms_contacts.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.list_sms_contacts.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.list_sms_contacts.setObjectName("list_sms_contacts")
        self.sms_area = QtWidgets.QTextEdit(self.tab_sms)
        self.sms_area.setGeometry(QtCore.QRect(430, 40, 591, 321))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.sms_area.setFont(font)
        self.sms_area.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.sms_area.setObjectName("sms_area")
        self.btn_send_sms = QtWidgets.QPushButton(self.tab_sms)
        self.btn_send_sms.setGeometry(QtCore.QRect(640, 400, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_send_sms.setFont(font)
        self.btn_send_sms.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_send_sms.setObjectName("btn_send_sms")
        self.tabWidget.addTab(self.tab_sms, "")
        self.tab_email = QtWidgets.QWidget()
        self.tab_email.setObjectName("tab_email")
        self.list_email_contacts = QtWidgets.QListWidget(self.tab_email)
        self.list_email_contacts.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.list_email_contacts.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.list_email_contacts.setObjectName("list_email_contacts")
        self.mailID_area = QtWidgets.QLineEdit(self.tab_email)
        self.mailID_area.setGeometry(QtCore.QRect(430, 40, 601, 41))
        self.mailID_area.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.mailID_area.setObjectName("mailID_area")
        self.mail_area = QtWidgets.QTextEdit(self.tab_email)
        self.mail_area.setGeometry(QtCore.QRect(430, 100, 601, 321))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mail_area.setFont(font)
        self.mail_area.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.mail_area.setObjectName("mail_area")
        self.btn_send_email = QtWidgets.QPushButton(self.tab_email)
        self.btn_send_email.setGeometry(QtCore.QRect(630, 440, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.btn_send_email.setFont(font)
        self.btn_send_email.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.btn_send_email.setObjectName("btn_send_email")
        self.tabWidget.addTab(self.tab_email, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Phonebook"))
        self.btn_add_contact.setText(_translate("Dialog", "  Add Contact  "))
        self.btn_backup.setText(_translate("Dialog", "Backup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_contacts), _translate("Dialog", "          Contacts            "))
        self.btn_send_vmsg.setText(_translate("Dialog", "Send Audio Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_voicemsg), _translate("Dialog", "          Audio Message         "))
        self.sms_area.setPlaceholderText(_translate("Dialog", "Type Message Here"))
        self.btn_send_sms.setText(_translate("Dialog", "Send Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sms), _translate("Dialog", "         SMS         "))
        self.mailID_area.setPlaceholderText(_translate("Dialog", "To  :    Email  ID  Here"))
        self.mail_area.setPlaceholderText(_translate("Dialog", "Type your Mail Here"))
        self.btn_send_email.setText(_translate("Dialog", "Send Mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_email), _translate("Dialog", "         Email          "))
