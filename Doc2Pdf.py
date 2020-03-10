import fix_qt_import_error
from Doc2PdfUI import Ui_MainWindow
from win32com.client import DispatchEx
import os
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *




class Doc2Pdf(object):
    def __init__(self):
        super().__init__()
        app = QtWidgets.QApplication(sys.argv)
        mainwindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainwindow)
        self.signal()
        mainwindow.show()
        sys.exit(app.exec_())

    def signal(self):
        if self.ui.FuncSelectCbox.currentText() == "单文件":
            self.ui.InputLocalBt.clicked.connect(self.chooseFileBt)
        self.ui.FuncSelectCbox.currentTextChanged.connect(self.comboBox_changed)
        self.ui.OutputLocalBt.clicked.connect(self.choosePdfDirBt)
        self.ui.StartBt.clicked.connect(self.StartBt)

    def chooseFileBt(self):

        file_name, file_type = QFileDialog.getOpenFileName(self.ui.centralwidget,"文件选择", os.getcwd(), "WORD files(*.doc *docx)")
        if file_name == " ":
            return
        if self.ui.InputCbox.findText(file_name) == -1:
            self.ui.InputCbox.addItem(file_name)
        self.ui.InputCbox.setCurrentIndex(self.ui.InputCbox.findText(file_name))


    def chooseDirBt(self):

        dir_name = QFileDialog.getExistingDirectory(self.ui.centralwidget, "选取文件夹", os.getcwd(),)
        if dir_name == "":
            return
        if self.ui.InputCbox.findText(dir_name) == -1:
            self.ui.InputCbox.addItem(dir_name)
        self.ui.InputCbox.setCurrentIndex(self.ui.InputCbox.findText(dir_name))


    def choosePdfDirBt(self):

        pdf_dir = QFileDialog.getExistingDirectory(self.ui.centralwidget,"选取文件夹",os.getcwd() ,)
        if pdf_dir == "":
            return
        if self.ui.OutputCbox.findText(pdf_dir) == -1:
            self.ui.OutputCbox.addItem(pdf_dir)
        self.ui.OutputCbox.setCurrentIndex(self.ui.OutputCbox.findText(pdf_dir))


    def comboBox_changed(self, text):
        if text == "批量":
            self.ui.InputLocalBt.clicked.disconnect(self.chooseFileBt)
            self.ui.InputLocalBt.clicked.connect(self.chooseDirBt)
        else:
            self.ui.InputLocalBt.clicked.disconnect(self.chooseDirBt)
            self.ui.InputLocalBt.clicked.connect(self.chooseFileBt)


    def StartBt(self):
        if self.ui.InputCbox.currentText() == "":
            reply = QMessageBox.information(self.ui.centralwidget, "笨媳妇","你瞅瞅是不是原文档路径没选")
            return
        if self.ui.OutputCbox.currentText() == "":
            reply = QMessageBox.information(self.ui.centralwidget, "笨媳妇","你瞅瞅是不是保存路径没选")
            return

        self.ui.StartBt.setText("正在努力呦")
        self.ui.StartBt.setEnabled(False)
        self.main1(self.ui.InputCbox.currentText(), self.ui.OutputCbox.currentText())
        reply = QMessageBox.information(self.ui.centralwidget, "臭媳妇", "完成啦")
        self.ui.StartBt.setEnabled(True)
        self.ui.StartBt.setText("开始")

    def fetchAllFile(self, path):
        files = []
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                ext = os.path.splitext(file)[1].lower()
                if ext == '.docx' or ext == '.doc':
                    fullpath = os.path.join(dirpath, file)
                    files.append(fullpath)
        return files


    def convertWordToPdf(self, docxPath, pdfPath):
        word = DispatchEx("Word.Application")
        try:
            doc = word.Documents.Open(docxPath)
            doc.SaveAs(pdfPath, FileFormat=17)
            doc.Close()
            word.Quit()
        except Exception as e:
            reply = QMessageBox.information(self.ui.centralwidget, "提示", e)
            print(e)


    def main1(self, docPath, pdfPath):
        self.ui.progressBar.setValue(0)
        if os.path.isfile(docPath):
            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(1)
            self.step = 0
            self.ui.progressBar.setValue(self.step)
            fileName = os.path.basename(docPath).split('.')[0] + '.pdf'
            savePath = os.path.join(pdfPath, fileName)
            if not os.path.exists(savePath):
                self.convertWordToPdf(docPath, savePath)
                self.step = self.step + 1
                self.ui.progressBar.setValue(self.step)
            else:
                reply = QMessageBox.information(self.ui.centralwidget, "提示","有同名文档存在")

        else:

            files = self.fetchAllFile(docPath)
            filesSum = int(len(files))
            step = 1

            self.ui.progressBar.setMinimum(0)
            self.ui.progressBar.setMaximum(len(files))
            for file in files:
                fileName = os.path.basename(file).split('.')[0] + '.pdf'
                savePath = os.path.join(pdfPath, fileName)

                if not os.path.exists(savePath):
                    self.convertWordToPdf(file, savePath)
                    self.ui.progressBar.setValue(step)
                    step = step + 1

                else:
                    reply = QMessageBox.information(self.ui.centralwidget, "提示","有同名文档存在")


if __name__ == '__main__':
    Doc2Pdf()