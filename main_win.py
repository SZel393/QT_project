# -*- coding: utf-8 -*-

import datetime as dt

from random import choice, randint, random

#from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from new_user import NewUser

from Ui_Main_win import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user, level, con):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.con = con
        self.user = user
        self.level = level
        # Выбор используемых систем счисления.
        # 2 - 2, 4, 8, 16 - ричные;
        # 1 - только 2, 4, 8;
        # 0 - только 2-ичная.
        if self.level[0] == '0':
            self.set_level_0()
        elif self.level[0] == '1':
            self.set_level_1()
        else:            
            self.set_level_2()
        if self.level[1] == '1':
            self.set_using_droby()
        else:
            self.set_off_using_droby()
        self.is_teacher = 0
        self.right = 0
        self.wrong = 0
        self.ur = 1
        self.up = 32  # Верхняя граница генерации случайных чисел.
        # Начинаем всегда с 1 - чтобы привыкнуть к интерфейсу
        self.s_to = "1"    
        self.answered = False
        self.tabWidget.setCurrentIndex(0)
        self.skip.clicked.connect(self.next_num)
        self.verify.clicked.connect(self.ver_num)

    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        self.update_stat()
        if index == 1:            
            self.user_stat()
        elif index == 3:
            self.user_stat_all()
        

    # Связь элементов вкладки "Настройка" с функциями настройки
    @pyqtSlot(bool)
    def on_radioButton_bin_only_toggled(self, checked):
        if checked:
            self.set_level_0()
            self.level = '0' + self.level[1]
        print('radioButton_bin_only', checked)

        
    @pyqtSlot(bool)
    def on_radioButton_2_4_8_toggled(self, checked):
        if checked:
            self.set_level_1()
            self.level = '1' + self.level[1]
        print('radioButton_2_4_8', checked)


    @pyqtSlot(bool)
    def on_radioButton_all_syst_toggled(self, checked):
        if checked:
            self.set_level_2()
            self.level = '2' + self.level[1]
        print('radioButton_all_syst', checked)

           
    @pyqtSlot(bool)
    def on_checkBox_droby_toggled(self, checked):
        if checked:
            self.set_using_droby()
            self.level = self.level[0] + '1'
        else:
            self.set_off_using_droby()
            self.level = self.level[0] + '0'
        print('checkBox_droby', checked)

    # Настройка доступных систем счисления и типов заданий
    def set_level_0(self):
        self.radioButton_bin_only.setChecked(True)
        self.osns = [2]
        self.funcs = {2: bin}
        self.friends = {2: [2]}
        self.names = {2: "двоичн", 10: "десятичн"}            
        self.tasks = [self.arifm, self.perevod_to_10, self.perevod_from_10]
        if self.level[1]:
            self.tasks.append(self.drobi)
            

    def set_level_1(self):
        self.radioButton_2_4_8.setChecked(True)
        self.osns = [2, 4, 8]
        self.funcs = {2: bin, 4: self.kvd, 8: oct}
        self.friends = {2: [4, 8], 4: [2], 8: [2]}
        self.names = {2: "двоичн", 4: "четверичн", 8: "восьмеричн", 10: "десятичн"}
        self.tasks = [self.friend, self.arifm, self.perevod_to_10, self.perevod_from_10]
        if self.level[1]:
            self.tasks.append(self.drobi)
        
    def set_level_2(self):
        self.radioButton_all_syst.setChecked(True)
        self.osns = [2, 4, 8, 16]
        self.funcs = {2: bin, 4: self.kvd, 8: oct, 16: hex}
        self.friends = {2: [4, 8, 16], 4: [2, 16], 8: [2], 16: [2, 4]}
        self.names = {2: "двоичн", 4: "четверичн", 8: "восьмеричн", 10: "десятичн", 16: "шестнадцитиричн"}
        self.tasks = [self.friend, self.arifm, self.perevod_to_10, self.perevod_from_10]
        if self.level[1]:
            self.tasks.append(self.drobi)

    def set_using_droby(self):
        self.checkBox_droby.setChecked(True)
        if self.drobi not in self.tasks:
            self.tasks.append(self.drobi)


    def set_off_using_droby(self):
        self.checkBox_droby.setChecked(False)
        if self.drobi in self.tasks:
            self.tasks.remove(self.drobi)  
               

    def set_teacher_mode(self, mode):
        if mode == '0':
            self.tabWidget.removeTab(3)
        self.is_teacher = mode
                       

    def kvd(self, x):
        # Простой способ перевода числа в 4-ричную сист.сч.
        s = bin(x)[2:]
        if len(s) % 2:
            s = '0' + s
        k = {"00": "0", "01": "1", "10": "2", "11": "3"}
        return "4x" + "".join(k[s[i: i + 2]] for i in range(0, len(s), 2))        


    # функции генерации задания возвращают кортеж:
    # (Текст задания, число для перевода/пример для вычисления, правильный ответ, подсказка)
    def drobi(self):
        # Перевод десятичных дробей в различные системы счисления
        # Используются только дроби, имеющие конечную запись в целевой с.сч.
        osn_to = choice(self.osns)
        x = randint(20, self.up)
        while True:
            y = randint(1, 20)
            drob = self.funcs[osn_to](y).upper()[2:]
            if y % osn_to != 0:
                break              
        problem = "Запишите значение данного десятичного  числа \n в " +\
                  self.names[osn_to] + "ой системе счисления. Используйте точку"
        cel = self.funcs[osn_to](x).upper()[2:]
        ans = cel + '.' + drob
        z = osn_to ** len(drob)
        q = x + y / z
        s_from = str(q)
        return (problem, s_from, ans, str(x) + '.' + str(y) + '/' + str(z))

    def friend(self):
        # Переводы в "дружественные" системы счисления
        osn_from = choice(self.osns)
        if len(self.friends[osn_from]) > 1:
            osn_to = choice(self.friends[osn_from])
        else:
            osn_to = self.friends[osn_from][0]
        problem = "Запишите значение данного " + self.names[osn_from] + "ого числа \n в " +\
                  self.names[osn_to] + "ой системе счисления"
        x = randint(1, self.up)
        s_from = self.funcs[osn_from](x)[2:]
        ans = self.funcs[osn_to](x)[2:]
        return (problem, s_from, ans, str(x))

    def arifm(self):
        # Выполнение арифметических операций в различных с.сч.
        osn = choice(self.osns)
        x = randint(1, self.up)
        problem = "Выполните арифметические действия. Ответ запишите в " +\
                  "той же системе счисления, что и исходные числа."
        if random() > 0.5:
            oper = '+'
            y = randint(1, self.up)
        elif random() > 0.25:
            oper = '-'
            y = randint(1, x)
        else:
            oper = '*'
            if random() > 0.33:
                y = osn
            else:
                y = osn ** 2
        s_from = self.funcs[osn](x)[2:].upper() + " " + oper + " " + self.funcs[osn](y)[2:].upper() + " = "
        ans10 = eval("{} {} {}".format(x, oper, y))
        ans = self.funcs[osn](ans10)[2:].upper()
        return (problem, s_from, ans, str(x) + " " + oper + " " + str(y) + ' = ' + str(ans10))

    def perevod_from_10(self):
        # Перевод из 10-й системы счисленияв в заданную только целых чисел
        osn_to = choice(self.osns)
        x = randint(1, self.up)
        problem = "Запишите значение данного десятичного  числа \n в " +\
                  self.names[osn_to] + "ой системе счисления."
        ans = self.funcs[osn_to](x).upper()[2:]
        s_from = str(x)
        return (problem, s_from, ans, "")            
        
    def perevod_to_10(self):
        # Перевод в 10-ю систему счисленияв ис заданной только целых чисел
        osn_from = choice(self.osns)
        x = randint(1, self.up)
        problem = "Запишите десятичное значение числа данного в \n" +\
                  self.names[osn_from] + "ой системе счисления."
        s_from = self.funcs[osn_from](x).upper()[2:]
        ans = str(x)
        return (problem, s_from, ans, "")            


    def next_num(self):
        # Выбирается произвольная из задач, допущенных на данном уровне
        task = choice(self.tasks)()
        # В режиме работы учителя видны правильные ответы (для проверки корректности)
        if self.is_teacher:
            print(task)
        self.problem.setText(task[0])
        self.task.setText(task[1])
        self.s_to = task[2]        
        self.remark.setText(" ")
        if not self.answered:
            self.wrong += 1
        self.ver.setText("Верных ответов " + str(self.right) +
                         "\nНеверных или пропущенных " + str(self.wrong))
        self.answered = False
        self.solution.setText("")
            

    def ver_num(self):

        # Возможно использование дробных чисел - проверяем
        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
            
        s = self.solution.text().strip()
        s = s.replace(',', '.')
        while len(s) > 1 and s[0] == '0':
            s = s[1:]
        is_digit = is_number(s)
        if is_digit and s == self.s_to and not self.answered:
            self.remark.setText("Верно")
            self.right += 1
            self.answered = True
        elif not is_digit:
            self.remark.setText("Это не число")
            self.answered = False
            self.wrong += 1
        elif self.answered:
            self.remark.setText("Ответ на этот вопрос уже был принят")
            self.wrong += 1           
        else:
            self.remark.setText("Неверно")
            self.answered = False
            self.wrong += 1
        self.ver.setText("Верных ответов " + str(self.right) +
                         "\nНеверных или пропущенных " + str(self.wrong))
        # Если работа идет успешно - повышаем верхнюю границу значений чисел
        if self.right > 2 * self.wrong:
            self.up += 10
        # Цвет меняется в зависимости от соотношения правильных - неправильных
        # (или пропущенных без ответа) заданий.
        # Это удобно, потому что видно издалека, насколько успешно илет работа.            
        if self.right > 4 * self.wrong + 1:
            self.ver.setStyleSheet("font-size: 18px;background-color: Aquamarine;")
        elif self.right > 2 * self.wrong + 1:
            self.ver.setStyleSheet("font-size: 18px;background-color: PaleGreen;")
        elif self.right > self.wrong:
            self.ver.setStyleSheet("font-size: 18px;background-color: Khaki;")
        elif self.right * 2 > self.wrong:
            self.ver.setStyleSheet("font-size: 18px;background-color: DarkOrange;")
        else:
            self.ver.setStyleSheet("font-size: 18px;background-color: OrangeRed;")

    # Заполнение статистики по текущему пользователю
    def user_stat(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT name, date, level, total, right from actions WHERE name = '{}'".format(self.user)).fetchall()
        n = len(res)
        print(res)
        self.tableUser.setRowCount(n)
        for i in range(n):
            for j in range(len(res[i])):
                self.tableUser.setItem(i, j, QTableWidgetItem(res[i][j]))
        
    # Заполнение статистики по всем пользователям
    def user_stat_all(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT name, date, level, total, right from actions").fetchall()
        res.sort()
        n = len(res)
        print(res)
        self.tableAllUser.setRowCount(n)
        for i in range(n):
            for j in range(len(res[i])):
                self.tableAllUser.setItem(i, j, QTableWidgetItem(res[i][j]))
        
    @pyqtSlot()
    # Вызов диалога добавления пользователя (модуль new_user.py)
    def on_pushButton_new_user_clicked(self):
        new_user_dialog = NewUser(self)
        new_user_dialog.set_connection(self.con)
        new_user_dialog.exec_()

    @pyqtSlot()
    def on_pushButton_export_stat_clicked(self):
        # Экспорт таблиц из базы данных в файлы формата csv с разделителем ";"
        # В название файла вписывается текущая дата и время для обеспечения уникальности
        cur = self.con.cursor()
        addnamefile = str(dt.date.today())
        r = cur.execute("SELECT * FROM users").fetchall()
        f = open('users' + addnamefile + ".csv", "w")
        f.write('Id;Name;Password;Is_teacher;Date_registration;Level\n')
        f.write('\n'.join(';'.join(map(str, [x for x in line])) for line in r))
        f.close()
        r = cur.execute("SELECT * FROM actions").fetchall()
        f = open('actions' + addnamefile + ".csv", "w")
        f.write('Id;Name;Date;Level;Right;Total\n')
        f.write('\n'.join(';'.join(map(str, [x for x in line])) for line in r))
        f.close()

    @pyqtSlot()
    def on_pushButton_clear_stat_clicked(self):
        # Очистка таблицы "actions"
        cur = self.con.cursor()
        cur.execute("DELETE FROM actions")
        self.con.commit()
        
    def update_stat(self):
        print('--->', self.user)
        if (self.wrong + self.right) > 0:
            cur = self.con.cursor()
            n = len(cur.execute("SELECT id FROM actions").fetchall())
            cur.execute("INSERT INTO actions VALUES({}, '{}', '{}', '{}', '{}', '{}')".format(n + 1, self.user,
                                                                                              str(dt.date.today()),self.level,
                                                                                              str(self.right),
                                                                                              str(self.right + self.wrong)))
            self.con.commit()
            self.right = 0
            self.wrong = 0
            self.ver.setText(" ")
