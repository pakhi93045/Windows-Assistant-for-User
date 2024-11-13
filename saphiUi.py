# Existing parts of the code
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saphi(object):
    def setupUi(self, saphi):
        saphi.setObjectName("saphi")
        saphi.resize(1152, 829)
        self.centralwidget = QtWidgets.QWidget(saphi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-30, 0, 1221, 821))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/7kmF.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Buttons and other components
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 730, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(238, 255, 189);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 730, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 118, 102);")
        self.pushButton_2.setObjectName("pushButton_2")

        # Date and Time Display (textBrowser and textBrowser_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 710, 201, 61))
        self.textBrowser.setStyleSheet("background: transparent; border: none; color: white; font-size: 20px;")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 630, 201, 61))
        self.textBrowser_2.setStyleSheet("background: transparent; border: none; color: white; font-size: 20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Logo or additional image
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 271, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Downloads/T8bahf (1).gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        saphi.setCentralWidget(self.centralwidget)

        self.retranslateUi(saphi)
        QtCore.QMetaObject.connectSlotsByName(saphi)

    def retranslateUi(self, saphi):
        _translate = QtCore.QCoreApplication.translate
        saphi.setWindowTitle(_translate("saphi", "MainWindow"))
        self.pushButton.setText(_translate("saphi", "Run"))
        self.pushButton_2.setText(_translate("saphi", "Terminate"))

# Main application execution
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saphi = QtWidgets.QMainWindow()
    ui = Ui_saphi()
    ui.setupUi(saphi)
    saphi.show()
    sys.exit(app.exec_())
