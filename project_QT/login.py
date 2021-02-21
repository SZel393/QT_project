# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from Ui_login import Ui_login


class Login(QDialog, Ui_login):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.name.setFocus(Qt.OtherFocusReason)
        self.user = ''
        self.is_teacher = 0

    def set_connection(self, connect):
        self.cur = connect.cursor()
        
    def accept(self):
        if self.password.text() == '' or self.name.text() == '':
            print(':(')
            return
        res = self.cur.execute("SELECT password, is_teacher from users WHERE name = '{}'".format(self.name.text())).fetchall()[0]
        if self.password.text() not in res:
            print(':(((')
            return
        self.user = self.name.text()
        self.is_teacher = res[1]
        super().accept()

        
