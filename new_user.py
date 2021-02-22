# -*- coding: utf-8 -*-

import datetime as dt

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from Ui_new_user import Ui_new_user


class NewUser(QDialog, Ui_new_user):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.name.setFocus(Qt.OtherFocusReason)


    def set_connection(self, connect):
        self.connect = connect
        self.cur = self.connect.cursor()


    def accept(self):
        name = self.name.text().strip()
        password = self.password.text().strip()
        r = self.cur.execute("SELECT id, name FROM users").fetchall()
        n = len(r)
        names = [x[1] for x in r]        
        if name == '':
            QMessageBox.critical(self, 
                                 'Ой...',
                                 'Нужно указать имя!',
                                 QMessageBox.Yes
                                )
            return

        if name in names:
            QMessageBox.critical(self, 
                                 'Ой...',
                                 'Нужно указать уникальное имя!',
                                 QMessageBox.Yes
                                )
            return

        if password == '':
            QMessageBox.critical(self, 
                                 'Ой...',
                                 'Нужно указать пароль!',
                                 QMessageBox.Yes
                                )
            return

        level = '0'
        if self.radioButton_bin_only.isChecked():
            pass
        elif self.radioButton_2_4_8.isChecked():
            level = '1'
        elif self.radioButton_all_syst.isChecked():
            level = '2'
        if self.checkBox_droby.isChecked():
            level += '1'
        else:
            level += '0'
        self.cur.execute("INSERT INTO users VALUES({}, '{}', '{}', '0', '{}', '{}')".format(n + 1, name, password, str(dt.date.today()), level))
        self.connect.commit()
        super().accept()
