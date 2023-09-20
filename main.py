from PyQt5 import QtCore, QtGui, QtWidgets

from CreateNewAccountsUI import CreateNewAccountsUI
from ImportExistingUserUI import ImportExistingUserUI
from SendEmailUI import SendEmailUI
from ViewCreatedAccountsTableUI import ViewCreatedAccountsUI


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 726)
        MainWindow.setMinimumSize(QtCore.QSize(1047, 726))
        MainWindow.setMaximumSize(QtCore.QSize(1047, 726))
        MainWindow.setStyleSheet("#title{\n"
"    background-color: #860f0f;\n"
"    color: white;\n"
"    padding-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #1f8a50;\n"
"    border: none;\n"
"    border-radius: 38px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #1f6450;\n"
"    border: none;\n"
"    border-radius: 38px;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #1f4e3a;\n"
"    border: none;\n"
"    border-radius: 38px;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 1047, 223))
        self.title.setMinimumSize(QtCore.QSize(1047, 223))
        self.title.setMaximumSize(QtCore.QSize(1047, 223))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.title.setObjectName("title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, -20, 206, 211))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(206, 211))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap("OU LOGO.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.importUserBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importUserBtn.setGeometry(QtCore.QRect(350, 240, 341, 90))
        self.importUserBtn.setMaximumSize(QtCore.QSize(384, 90))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        self.importUserBtn.setFont(font)
        self.importUserBtn.setObjectName("importUserBtn")
        self.createAccBtn = QtWidgets.QPushButton(self.centralwidget)
        self.createAccBtn.setGeometry(QtCore.QRect(350, 350, 341, 90))
        self.createAccBtn.setMaximumSize(QtCore.QSize(384, 90))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        self.createAccBtn.setFont(font)
        self.createAccBtn.setObjectName("createAccBtn")
        self.viewAccBtn = QtWidgets.QPushButton(self.centralwidget)
        self.viewAccBtn.setGeometry(QtCore.QRect(350, 460, 341, 90))
        self.viewAccBtn.setMaximumSize(QtCore.QSize(384, 90))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        self.viewAccBtn.setFont(font)
        self.viewAccBtn.setObjectName("viewAccBtn")
        self.sendEmailBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendEmailBtn.setGeometry(QtCore.QRect(350, 570, 341, 90))
        self.sendEmailBtn.setMaximumSize(QtCore.QSize(384, 90))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(20)
        self.sendEmailBtn.setFont(font)
        self.sendEmailBtn.setObjectName("sendEmailBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.importUserBtn.clicked.connect(self.openExistingUserUI)
        self.createAccBtn.clicked.connect(self.openCreateNewAccountsUI)
        self.viewAccBtn.clicked.connect(self.openViewCreatedAccountsUI)
        self.sendEmailBtn.clicked.connect(self.openSendEmailUI)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def openExistingUserUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ImportExistingUserUI(self.window)
        self.ui.setupUi(self.window)
        self.window.show()
        #self.ui.show()

    def openCreateNewAccountsUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = CreateNewAccountsUI(self.window)
        self.ui.setupUi(self.window)
        self.window.show()

    def openViewCreatedAccountsUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ViewCreatedAccountsUI()
        self.ui.setupUi(self.window)
        self.window.show()

    def openSendEmailUI(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = SendEmailUI(self.window)
        self.ui.setupUi(self.window)
        self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UP Google Email Generator"))
        self.title.setText(_translate("MainWindow", "UP Google Email Generator"))
        self.importUserBtn.setText(_translate("MainWindow", "Import Existing User"))
        self.createAccBtn.setText(_translate("MainWindow", "Create New Accounts"))
        self.viewAccBtn.setText(_translate("MainWindow", "View Created Accounts"))
        self.sendEmailBtn.setText(_translate("MainWindow", "Send Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    MainWindow.show()
    sys.exit(app.exec_())
