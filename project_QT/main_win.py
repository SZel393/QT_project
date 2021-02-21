# -*- coding: utf-8 -*-

#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from Ui_Main_win import Ui_MainWindow
from random import choice, randint


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.osns = [2, 4, 8, 16]
        self.funcs = {2: bin, 4: self.kvd, 8: oct, 16: hex}
        self.friends = {2: [4, 8], 4: [2], 8: [2], 16: [2, 4]}
        self.names = {2: "двоичн", 4: "четверичн", 8: "восьмеричн", 10: "десятичн", 16: "шестнадцитиричн"}
        self.right = 0
        self.wrong = 0
        self.ur = 1
        self.up = 32
        self.x = 1
        self.s_to = "1"
        self.answered = False
        self.skip.clicked.connect(self.next_num)
        self.verify.clicked.connect(self.ver_num)


    def set_teacher_mode(self, mode):
        if not mode:
            print('hide teacher part')
#            self.teacher.setEnabled(False)
#            self.teacher.setVisible(False)
#            self.tabWidget.setTabEnabled(3, False)
            self.tabWidget.removeTab(3)
            
            

    def kvd(self, x):
        s = bin(x)[2:]
        if len(s) % 2:
            s = '0' + s
        k = {"00": "0", "01": "1", "10": "2", "11": "3"}
        return "4x" + "".join(k[s[i: i + 2]] for i in range(0, len(s), 2))        

    def next_num(self):
        osn_to = choice(self.osns)
        self.x = randint(20, self.up)
        while True:
            self.y = randint(1, 20)
            drob = self.funcs[osn_to](self.y).upper()[2:]
            if self.y % osn_to != 0:
                break              
        print(self.x, self.y)
        self.problem.setText("Запишите значение данного десятичного  числа \n в " +\
                         self.names[osn_to] + "ой системе счисления. Используйте точку")
        print(drob)
        cel = self.funcs[osn_to](self.x).upper()[2:]
        print(cel)
        ans = cel + '.' + drob
        print(ans)
        self.z = osn_to ** len(drob)
        print(self.z)
        q = self.x + self.y / self.z
        print(q)
        self.s_from = str(q)
        print(' from', self.s_from)
        self.s_to = ans
        self.task.setText(self.s_from)
        self.remark.setText(" ")
        if not self.answered:
            self.wrong += 1
        self.ver.setText("Верных ответов " + str(self.right) +
                         "\nНеверных или пропущенных " + str(self.wrong))
        self.answered = False
        self.solution.setText("")

            

    def ver_num(self):
        
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
            
        s = self.solution.text().strip()
        s = s.replace(',', '.')
        print('ver right', self.s_to, 'ans', s)
        while len(s) > 1 and s[0] == '0':
            s = s[1:]
        is_digit = is_number(s)
        if is_digit and s == self.s_to and not self.answered:
            self.remark.setText("верно")
            self.right += 1
            self.answered = True
        elif not is_digit:
            self.remark.setText("это не число")
            self.answered = False
            self.wrong += 1
        elif self.answered:
            self.remark.setText("этот ответ уже принят")
            self.wrong += 1           
        else:
            self.remark.setText("неверно")
            self.answered = False
            self.wrong += 1
        self.ver.setText("Верных ответов " + str(self.right) +
                         "\nНеверных или пропущенных " + str(self.wrong))
        if self.right > 2 * self.wrong:
            self.up += 10
        if self.right > 4 * self.wrong + 1:
            self.ver.setStyleSheet("font-size: 24px; background-color: Aquamarine;")
        elif self.right > 2 * self.wrong + 1:
            self.ver.setStyleSheet("font-size: 24px; background-color: PaleGreen;")
        elif self.right > self.wrong:
            self.ver.setStyleSheet("font-size: 24px; background-color: Khaki;")
        elif self.right * 2 > self.wrong:
            self.ver.setStyleSheet("font-size: 24px; background-color: DarkOrange;")
        else:
            self.ver.setStyleSheet("font-size: 24px; background-color: OrangeRed;")
            
