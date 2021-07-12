# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 457)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(239, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 70, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 150, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.qu = QtWidgets.QLineEdit(self.centralwidget)
        self.qu.setGeometry(QtCore.QRect(500, 120, 301, 31))
        self.qu.setObjectName("qu")
        self.an = QtWidgets.QLineEdit(self.centralwidget)
        self.an.setGeometry(QtCore.QRect(500, 200, 311, 31))
        self.an.setObjectName("an")
        self.qb = QtWidgets.QComboBox(self.centralwidget)
        self.qb.setGeometry(QtCore.QRect(500, 50, 171, 22))
        self.qb.setObjectName("qb")
        self.ad = QtWidgets.QPushButton(self.centralwidget)
        self.ad.setGeometry(QtCore.QRect(630, 410, 75, 23))
        self.ad.setObjectName("ad")
        self.dis = QtWidgets.QTextEdit(self.centralwidget)
        self.dis.setGeometry(QtCore.QRect(20, 30, 411, 301))
        self.dis.setObjectName("dis")
        self.q = QtWidgets.QTextEdit(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(20, 350, 301, 71))
        self.q.setObjectName("q")
        self.s = QtWidgets.QPushButton(self.centralwidget)
        self.s.setGeometry(QtCore.QRect(340, 350, 91, 71))
        self.s.setObjectName("s")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 30, 20, 401))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tr = QtWidgets.QPushButton(self.centralwidget)
        self.tr.setGeometry(QtCore.QRect(660, 250, 75, 23))
        self.tr.setObjectName("tr")
        self.nt = QtWidgets.QLineEdit(self.centralwidget)
        self.nt.setGeometry(QtCore.QRect(560, 370, 191, 31))
        self.nt.setObjectName("nt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 320, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(490, 290, 321, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.ab = QtWidgets.QPushButton(self.centralwidget)
        self.ab.setGeometry(QtCore.QRect(570, 250, 75, 23))
        self.ab.setObjectName("ab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AI-BOT"))
        self.label.setText(_translate("MainWindow", "Topic"))
        self.label_2.setText(_translate("MainWindow", "Question"))
        self.label_3.setText(_translate("MainWindow", "Answer"))
        self.ad.setText(_translate("MainWindow", "Add"))
        self.s.setText(_translate("MainWindow", "Send"))
        self.tr.setText(_translate("MainWindow", "Train"))
        self.label_4.setText(_translate("MainWindow", "New Topic"))
        self.ab.setText(_translate("MainWindow", "Append"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
