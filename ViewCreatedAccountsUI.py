from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow

import csv

class ViewCreatedAccountsUI(object):
    newly_created_accounts = "RV_new_uploads.csv"

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

        self.editTextEdit()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def editTextEdit(self):
        try:
            with open(self.newly_created_accounts, "r") as csv_file:
                # Make a variable to parse the csv
                csv_reader = csv.reader(csv_file)

                msg = ""
                next(csv_reader)
                # Use for loops to see each line
                msg += "Newly Created Users:"
                for line in csv_reader:
                    msg += "\n"
                    msg += "\n" + "-"*40
                    msg += f"\nEmail Address: {line[0]}"
                    msg += f"\nFirst Name: {line[1]}"
                    msg += f"\nLast Name: {line[2]}"
                    msg += f"\nOrg Unit Path: {line[3]}"
                    msg += f"\nRecovery Email: {line[4]}"
                    msg += f"\nPassword: {line[5]}"
                    msg += "\n" + "-"*40

                self.createdAccountsEntry.setText(msg)
        except FileNotFoundError:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please make sure that 'RV_new_uploads.csv' is in the same directory")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "View Created Accounts"))
        self.title.setText(_translate("MainWindow", "View Created Accounts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewCreatedAccountsUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
