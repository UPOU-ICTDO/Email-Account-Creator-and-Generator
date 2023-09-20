import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class ViewCreatedAccountsUI(object):
    newly_created_accounts = "RV_new_uploads.csv"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 683)
        MainWindow.setMinimumSize(QtCore.QSize(601, 683))
        MainWindow.setMaximumSize(QtCore.QSize(601, 683))
        MainWindow.setStyleSheet("#title{\n"
"    background-color: #860f0f;\n"
"    color: white;\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"    border: 1px solid black;\n"
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
        self.createdAccountsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.createdAccountsTable.setGeometry(QtCore.QRect(20, 110, 561, 561))
        self.createdAccountsTable.setAutoFillBackground(False)
        self.createdAccountsTable.setStyleSheet("QHeaderView::section{\n"
"    border: none;\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    color: black;\n"
"    padding: 5px;\n"
"}\n"
"")
        self.createdAccountsTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.createdAccountsTable.setFrameShadow(QtWidgets.QFrame.Plain)
        self.createdAccountsTable.setLineWidth(2)
        self.createdAccountsTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.createdAccountsTable.setDragDropOverwriteMode(False)
        self.createdAccountsTable.setAlternatingRowColors(True)
        self.createdAccountsTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.createdAccountsTable.setGridStyle(QtCore.Qt.SolidLine)
        self.createdAccountsTable.setWordWrap(True)
        self.createdAccountsTable.setCornerButtonEnabled(True)
        self.createdAccountsTable.setObjectName("createdAccountsTable")
        self.createdAccountsTable.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.createdAccountsTable.setHorizontalHeaderItem(6, item)
        self.createdAccountsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.createdAccountsTable.horizontalHeader().setDefaultSectionSize(150)
        self.createdAccountsTable.horizontalHeader().setSortIndicatorShown(True)
        self.createdAccountsTable.horizontalHeader().setStretchLastSection(False)
        self.createdAccountsTable.verticalHeader().setVisible(False)
        self.createdAccountsTable.verticalHeader().setCascadingSectionResizes(False)
        self.createdAccountsTable.verticalHeader().setDefaultSectionSize(30)
        self.createdAccountsTable.verticalHeader().setStretchLastSection(False)
        MainWindow.setCentralWidget(self.centralwidget)

        #self.addNewCreatedAccounts()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "View Created Accounts"))
        self.title.setText(_translate("MainWindow", "View Created Accounts"))
        self.createdAccountsTable.setSortingEnabled(False)
        item = self.createdAccountsTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No."))
        item = self.createdAccountsTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email Address"))
        item = self.createdAccountsTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.createdAccountsTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.createdAccountsTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Org Unit Path"))
        item = self.createdAccountsTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Recovery Email"))
        item = self.createdAccountsTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Password"))
        __sortingEnabled = self.createdAccountsTable.isSortingEnabled()
        self.createdAccountsTable.setSortingEnabled(False)

        try:
            with open(self.newly_created_accounts, "r") as csv_file:
                # Make a variable to parse the csv

                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                csv_reader = list(csv_reader)

            counter = 1
            for line in csv_reader:
                rowCount = self.createdAccountsTable.rowCount()
                self.createdAccountsTable.insertRow(rowCount)
                line.insert(0, counter)
                for i in range(len(line)):
                    #line.insert(0, i)
                    print(line[i])
                    self.createdAccountsTable.setItem(rowCount, i, QTableWidgetItem(str(line[i])))
                print("------")
                counter += 1
        except FileNotFoundError:
            msg = QMessageBox()
            msg.setWindowTitle("Error!")
            msg.setText("Please make sure that 'RV_new_uploads.csv' is in the same directory")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ViewCreatedAccountsUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
