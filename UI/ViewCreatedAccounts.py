# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View Created Accounts.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 595)
        MainWindow.setStyleSheet("#title{\n"
"    background-color: #860f0f;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #1f8a50;\n"
"    border: none;\n"
"    border-radius: 28px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #1f6450;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #1f4e3a;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;    \n"
"}")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 601, 91))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.createdAccountsEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.createdAccountsEntry.setGeometry(QtCore.QRect(20, 110, 561, 471))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.createdAccountsEntry.setFont(font)
        self.createdAccountsEntry.setObjectName("createdAccountsEntry")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Created Accounts"))
        self.title.setText(_translate("MainWindow", "View Created Accounts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
