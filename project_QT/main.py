#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import sqlite3
import os.path
import datetime as dt

from PyQt5.QtWidgets import QApplication
from login import Login
from main_win import MainWindow

if os.path.isfile("systems.sqlite"):
    con = sqlite3.connect("systems.sqlite")
    cur = con.cursor()
else:   
    con = sqlite3.connect("systems.sqlite")
    cur = con.cursor()
    cur.execute("CREATE TABLE users(id integer PRIMARY KEY, name text, password text, is_teacher text, date text, level text)")
    cur.execute("INSERT INTO users VALUES(1, 'Lana', '54321', '1', '2020-10-21', '21')")
    cur.execute("INSERT INTO users VALUES(2, 'NoName', '123', '0', '2020-10-21', '00')")
    cur.execute("CREATE TABLE actions(id integer PRIMARY KEY, name text, date text, level text, right text, total text)")
    con.commit()
                
app = QApplication(sys.argv)
login = Login()
login.set_connection(con)
ok = login.exec_()
print(ok, login.name.text(), login.password.text())

if ok:
    main_win = MainWindow(login.name.text(), login.level, con)
    main_win.set_teacher_mode(login.is_teacher)
    main_win.show()
    app.exec_()
    n = len(cur.execute("SELECT id FROM actions").fetchall())
    cur.execute("INSERT INTO actions VALUES({}, '{}', '{}', '{}', '{}', '{}')".format(n + 1,
                                                                                      login.user,
                                                                                      str(dt.date.today()), main_win.level,
                                                                                      str(main_win.right),
                                                                                      str(main_win.right + main_win.wrong)))
    cur.execute("UPDATE users SET level = '{}' WHERE id == {}".format(main_win.level, login.user_id))
    con.commit()
    con.close()
    

