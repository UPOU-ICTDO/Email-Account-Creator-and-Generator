from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox, QMainWindow

from createAccounts import main


class CreateNewAccountsUI(object):
    def __init__(self, win):
        self.win = win

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 367)
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
        self.pathToImportCsvEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.pathToImportCsvEntry.setGeometry(QtCore.QRect(30, 140, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.pathToImportCsvEntry.setFont(font)
        self.pathToImportCsvEntry.setObjectName("pathToImportCsvEntry")
        self.findCsvBtn = QtWidgets.QPushButton(self.centralwidget)
        self.findCsvBtn.setGeometry(QtCore.QRect(390, 140, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.findCsvBtn.setFont(font)
        self.findCsvBtn.setObjectName("findCsvBtn")
        self.findCsvBtn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.findCsvBtn_2.setGeometry(QtCore.QRect(150, 260, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(16)
        self.findCsvBtn_2.setFont(font)
        self.findCsvBtn_2.setObjectName("findCsvBtn_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.file_name = ""

        self.findCsvBtn.clicked.connect(self.openFileDialog)
        self.findCsvBtn_2.clicked.connect(self.insertToDatabase)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openFileDialog(self):
        self.pathToImportCsvEntry.setText("")
        self.file_name = QFileDialog.getOpenFileName(self.win, 'Open CSV File', "", 'CSV Files (*.csv)')
        self.pathToImportCsvEntry.setText(self.file_name[0])

    def insertToDatabase(self):
        if self.file_name:
            try:
                main(self.file_name[0])
                msg = QMessageBox()
                msg.setWindowTitle("Successful!")
                msg.setText("Created New Accounts!\n\nSaved in RV_new_uploads.csv")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("Error!")
                msg.setText("Please make sure that you selected the right CSV File.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                x = msg.exec_()
        else:
            msg = QMessageBox(self.win)
            msg.setWindowTitle("Error!")
            msg.setText("Please make sure that you selected a CSV File.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Import CSV File"))
        self.title.setText(_translate("MainWindow", "Create New Accounts"))
        self.pathToImportCsvEntry.setPlaceholderText(_translate("MainWindow", "path/to/newAccounts.csv"))
        self.findCsvBtn.setText(_translate("MainWindow", "Find CSV File"))
        self.findCsvBtn_2.setText(_translate("MainWindow", "Insert to Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = CreateNewAccountsUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
