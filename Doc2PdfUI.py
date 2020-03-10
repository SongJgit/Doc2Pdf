# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Doc2PdfUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.FunSelectLb = QtWidgets.QLabel(self.centralwidget)
        self.FunSelectLb.setMaximumSize(QtCore.QSize(60, 16777215))
        self.FunSelectLb.setObjectName("FunSelectLb")
        self.gridLayout.addWidget(self.FunSelectLb, 0, 0, 1, 1)
        self.OutputFileLb = QtWidgets.QLabel(self.centralwidget)
        self.OutputFileLb.setObjectName("OutputFileLb")
        self.gridLayout.addWidget(self.OutputFileLb, 2, 0, 1, 1)
        self.FuncSelectCbox = QtWidgets.QComboBox(self.centralwidget)
        self.FuncSelectCbox.setMinimumSize(QtCore.QSize(0, 35))
        self.FuncSelectCbox.setObjectName("FuncSelectCbox")
        self.gridLayout.addWidget(self.FuncSelectCbox, 0, 1, 1, 2)
        self.OutputLocalBt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputLocalBt.sizePolicy().hasHeightForWidth())
        self.OutputLocalBt.setSizePolicy(sizePolicy)
        self.OutputLocalBt.setMaximumSize(QtCore.QSize(70, 35))
        self.OutputLocalBt.setObjectName("OutputLocalBt")
        self.gridLayout.addWidget(self.OutputLocalBt, 2, 2, 1, 1)
        self.StartBt = QtWidgets.QPushButton(self.centralwidget)
        self.StartBt.setMaximumSize(QtCore.QSize(406, 35))
        self.StartBt.setObjectName("StartBt")
        self.gridLayout.addWidget(self.StartBt, 3, 1, 1, 1)
        self.InputCbox = QtWidgets.QComboBox(self.centralwidget)
        self.InputCbox.setMinimumSize(QtCore.QSize(0, 35))
        self.InputCbox.setObjectName("InputCbox")
        self.gridLayout.addWidget(self.InputCbox, 1, 1, 1, 1)
        self.InputFileLb = QtWidgets.QLabel(self.centralwidget)
        self.InputFileLb.setObjectName("InputFileLb")
        self.gridLayout.addWidget(self.InputFileLb, 1, 0, 1, 1)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 3)

        self.InputLocalBt = QtWidgets.QPushButton(self.centralwidget)
        self.InputLocalBt.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputLocalBt.sizePolicy().hasHeightForWidth())
        self.InputLocalBt.setSizePolicy(sizePolicy)
        self.InputLocalBt.setMinimumSize(QtCore.QSize(0, 0))
        self.InputLocalBt.setMaximumSize(QtCore.QSize(70, 35))
        self.InputLocalBt.setObjectName("InputLocalBt")
        self.gridLayout.addWidget(self.InputLocalBt, 1, 2, 1, 1)
        self.OutputCbox = QtWidgets.QComboBox(self.centralwidget)
        self.OutputCbox.setMinimumSize(QtCore.QSize(0, 35))
        self.OutputCbox.setObjectName("OutputCbox")
        self.gridLayout.addWidget(self.OutputCbox, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOR MY HQ"))
        self.FunSelectLb.setText(_translate("MainWindow", "选择："))
        self.OutputFileLb.setText(_translate("MainWindow", "输出位置："))
        self.OutputLocalBt.setText(_translate("MainWindow", "浏览..."))
        self.StartBt.setText(_translate("MainWindow", "开始"))
        self.InputFileLb.setText(_translate("MainWindow", "输入文件："))
        self.InputLocalBt.setText(_translate("MainWindow", "浏览..."))
        self.FuncSelectCbox.addItem("单文件")
        self.FuncSelectCbox.addItem("批量")