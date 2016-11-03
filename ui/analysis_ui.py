# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created: Thu Nov 03 11:17:12 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Analysis(object):
    def setupUi(self, Analysis):
        Analysis.setObjectName("Analysis")
        Analysis.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Analysis.sizePolicy().hasHeightForWidth())
        Analysis.setSizePolicy(sizePolicy)
        Analysis.setMinimumSize(QtCore.QSize(400, 320))
        Analysis.setMaximumSize(QtCore.QSize(1024, 800))
        self.centralwidget = QtGui.QWidget(Analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(671, 180, 101, 51))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(671, 250, 101, 51))
        self.stopButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stopButton.setObjectName("stopButton")
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(31, 110, 471, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.loopNum = QtGui.QSpinBox(self.centralwidget)
        self.loopNum.setGeometry(QtCore.QRect(290, 10, 46, 22))
        self.loopNum.setObjectName("loopNum")
        self.timePerLoop = QtGui.QSpinBox(self.centralwidget)
        self.timePerLoop.setGeometry(QtCore.QRect(370, 10, 46, 22))
        self.timePerLoop.setObjectName("timePerLoop")
        self.filePickerButton2 = QtGui.QPushButton(self.centralwidget)
        self.filePickerButton2.setEnabled(False)
        self.filePickerButton2.setGeometry(QtCore.QRect(451, 190, 51, 31))
        self.filePickerButton2.setObjectName("filePickerButton2")
        self.basePath = QtGui.QLineEdit(self.centralwidget)
        self.basePath.setEnabled(False)
        self.basePath.setGeometry(QtCore.QRect(31, 190, 411, 31))
        self.basePath.setObjectName("basePath")
        self.filePickerButton = QtGui.QPushButton(self.centralwidget)
        self.filePickerButton.setGeometry(QtCore.QRect(451, 70, 51, 31))
        self.filePickerButton.setObjectName("filePickerButton")
        self.roverPath = QtGui.QLineEdit(self.centralwidget)
        self.roverPath.setGeometry(QtCore.QRect(31, 70, 411, 31))
        self.roverPath.setObjectName("roverPath")
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(31, 50, 141, 18))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(31, 170, 141, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.resolveAllButton = QtGui.QPushButton(self.centralwidget)
        self.resolveAllButton.setGeometry(QtCore.QRect(670, 60, 101, 51))
        self.resolveAllButton.setObjectName("resolveAllButton")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 320, 471, 261))
        self.textBrowser.setObjectName("textBrowser")
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 230, 471, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        Analysis.setCentralWidget(self.centralwidget)

        self.retranslateUi(Analysis)
        QtCore.QMetaObject.connectSlotsByName(Analysis)

    def retranslateUi(self, Analysis):
        Analysis.setWindowTitle(QtGui.QApplication.translate("Analysis", "Raw Measurement Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.startButton.setText(QtGui.QApplication.translate("Analysis", "start analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("Analysis", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.filePickerButton2.setText(QtGui.QApplication.translate("Analysis", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.filePickerButton.setText(QtGui.QApplication.translate("Analysis", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Analysis", "Rover Raw/RTCM file:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("Analysis", "Base Raw/RTCM file:", None, QtGui.QApplication.UnicodeUTF8))
        self.resolveAllButton.setText(QtGui.QApplication.translate("Analysis", "analysis all", None, QtGui.QApplication.UnicodeUTF8))

