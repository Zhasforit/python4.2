#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        #self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        text2 = self.textEdit_words.toPlainText()
        vyrez = []
        for i in range(len(text2)):
            if text2[i] == " ":
                vyrez.append(0)
            if text2[i] == "\n" and text2[i-1] != "\n":
                vyrez.append(1)
        vyrez.append(1)
        txt = text.split()
        txt2 = text2.split()
        stroka = ""
        for i in txt2:
            for j in txt:
                if i == j:
                    slovo = i.upper()
                    txt2[txt2.index(j)] = slovo
                    break
        for j in range(len(txt2)):
            if vyrez[j] == 0:
                stroka += txt2[j] + " "
            if vyrez[j] == 1:
                stroka += txt2[j] + "\n"
        self.textEdit_words.setPlainText(stroka)

        #for s in txt:
        #    self.textEdit_words.insertPlainText(s.upper()+" ")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
