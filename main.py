import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from PyQt5.QtWidgets import QBoxLayout


page1 = uic.loadUiType("test2.ui")[0]

class MainWindow(QMainWindow, page1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect("test.db",isolation_level=None)
        self.cur = self.conn.cursor()
        self.i = 0
        self.happy_point = 0
        self.dp_point = 0
        self.t_start_1.clicked.connect(self.happy)
        self.next_1.clicked.connect(self.happy2)
        self.next_2.clicked.connect(self.happy3)
        self.next_3.clicked.connect(self.happy4)
        self.next_4.clicked.connect(self.happy_end)
        self.next_5.clicked.connect(self.next)
        self.next_6.clicked.connect(self.depression2)
        self.next_7.clicked.connect(self.depression_end)
        self.t_start_2.clicked.connect(self.depression)
        self.end_1.clicked.connect(self.end)
        self.end_2.clicked.connect(self.end)
        self.end_3.clicked.connect(self.end)
        self.pageup = 1
    def graph(self):
        self.end()
        self.cur.execute("SELECT * from user WHERE happy >=41")                 # happy 41 이상 호출
        result = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy >= 41")  # depression 평균 호출
        result1 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result))
        happy = []
        for i in range(len(result)):
            happy.append(result[i][1])
        print(len(happy))
        print(result1[0][0])

        self.cur.execute("SELECT * from user WHERE happy < 41 and happy >= 30")      # happy 41 미만 30이상 호출
        result2 = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy < 41 and happy >= 30")  # depression 평균 호출
        result3 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result1))
        happy1 = []
        for i in range(len(result2)):
            happy1.append(result2[i][1])
        print(len(happy1))
        print(result3[0][0])

        self.cur.execute("SELECT * from user WHERE happy <=29")              # happy 29 이하 호출
        result4 = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy <=29")  # depression 평균 호출
        result5 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result2))
        happy2 = []
        for i in range(len(result4)):
            happy2.append(result4[i][1])
        print(len(happy2))
        print(result5[0][0])


    def depression_end(self):
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        if ( self.y_9_1.isChecked() == True or self.y_9_2.isChecked() == True or self.y_9_3.isChecked() == True or self.y_9_4.isChecked() == True):
            self.b = 0
        if (self.y_10_1.isChecked() == True or self.y_10_2.isChecked() == True or self.y_10_3.isChecked() == True or self.y_10_4.isChecked() == True):
            self.c = 0
        if (self.y_11_1.isChecked() == True or self.y_11_2.isChecked() == True or self.y_11_3.isChecked() == True or self.y_11_4.isChecked() == True):
            self.d = 0
        if (self.y_12_1.isChecked() == True or self.y_12_2.isChecked() == True or self.y_12_3.isChecked() == True or self.y_12_4.isChecked() == True):
            self.e = 0
        if (self.y_13_1.isChecked() == True or self.y_13_2.isChecked() == True or self.y_13_3.isChecked() == True or self.y_13_4.isChecked() == True):
            self.f = 0
        if (self.y_14_1.isChecked() == True or self.y_14_2.isChecked() == True or self.y_14_3.isChecked() == True or self.y_14_4.isChecked() == True):
            self.g = 0
        if (self.y_15_1.isChecked() == True or self.y_15_2.isChecked() == True or self.y_15_3.isChecked() == True or self.y_15_4.isChecked() == True):
            self.h = 0

        if (self.b == self.c == self.d == self.e == self.f == self.g == self.h):

            self.pageup += 1
            self.main.setCurrentIndex(self.pageup)
            if (self.y_9_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_9_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_9_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_9_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_10_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_10_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_10_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_10_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_11_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_11_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_11_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_11_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_12_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_12_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_12_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_12_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_13_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_13_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_13_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_13_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_14_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_14_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_14_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_14_4.isChecked() == True):
                self.dp_point += 0
            if (self.y_15_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_15_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_15_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_15_4.isChecked() == True):
                self.dp_point += 0
            print(self.dp_point)

            self.j_2.setText("당신의 점수는 {}점입니다.".format(self.dp_point))
            if (self.dp_point >=31):
                self.endt_1.setText("심한 우울 상태입니다.")
                self.endt_2.setText("전문가와 함께 우울한 상태를 극복하기 위한 적극적인 노력이 필요합니다.")
            elif (self.dp_point >= 21):
                self.endt_1.setText("무시하기 힘든 우울 상태입니다.")
                self.endt_2.setText("우울 상태를 극복하기 위한 적극적인 노력이 필요합니다.")
            elif (self.dp_point >= 11):
                self.endt_1.setText("정상적이지만 가벼운 우울 상태입니다.")
                self.endt_2.setText("자신의 기분을 새롭게 전환할 수 있는 노력이 필요합니다.")
            else:
                self.endt_1.setText("현재 우울하지 않은 상태입니다.")

            print("update3")
            self.cur.execute(
                "UPDATE user set depression = '{}' WHERE user_name = '{}'".format(self.dp_point, self.nickname))
            print("update4")
        else:
            print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')

    def depression2(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        if (self.y_1_1.isChecked() == True or self.y_1_2.isChecked() == True or self.y_1_3.isChecked() == True or self.y_1_4.isChecked() == True):
            self.a = 0
        if (self.y_2_1.isChecked() == True or self.y_2_2.isChecked() == True or self.y_2_3.isChecked() == True or self.y_2_4.isChecked() == True):
            self.b = 0
        if (self.y_3_1.isChecked() == True or self.y_3_2.isChecked() == True or self.y_3_3.isChecked() == True or self.y_3_4.isChecked() == True):
            self.c = 0
        if (self.y_4_1.isChecked() == True or self.y_4_2.isChecked() == True or self.y_4_3.isChecked() == True or self.y_4_4.isChecked() == True):
            self.d = 0
        if (self.y_5_1.isChecked() == True or self.y_5_2.isChecked() == True or self.y_5_3.isChecked() == True or self.y_5_4.isChecked() == True):
            self.e = 0
        if (self.y_6_1.isChecked() == True or self.y_6_2.isChecked() == True or self.y_6_3.isChecked() == True or self.y_6_4.isChecked() == True):
            self.f = 0
        if (self.y_7_1.isChecked() == True or self.y_7_2.isChecked() == True or self.y_7_3.isChecked() == True or self.y_7_4.isChecked() == True):
            self.g = 0
        if (self.y_8_1.isChecked() == True or self.y_8_2.isChecked() == True or self.y_8_3.isChecked() == True or self.y_8_4.isChecked() == True):
            self.h = 0

        if (self.a == self.b == self.c == self.d == self.e == self.f == self.g == self.h):

            if (self.y_1_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_1_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_1_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_1_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_2_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_2_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_2_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_2_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_3_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_3_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_3_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_3_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_4_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_4_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_4_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_4_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_5_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_5_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_5_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_5_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_6_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_6_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_6_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_6_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_7_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_7_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_7_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_7_4.isChecked() == True):
                self.dp_point += 0

            if (self.y_8_1.isChecked() == True):
                self.dp_point += 3
            elif (self.y_8_2.isChecked() == True):
                self.dp_point += 2
            elif (self.y_8_3.isChecked() == True):
                self.dp_point += 1
            elif (self.y_8_4.isChecked() == True):
                self.dp_point += 0

            self.depression2page()
        else:
            print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')
    def depression2page(self):
        print(self.dp_point)
        self.pageup += 1
        self.main.setCurrentIndex(self.pageup)
        self.cur.execute("SELECT text FROM test_depression")
        result = self.cur.fetchall()
        self.conn.commit()
        #
        self.text_y_9.setText("{}".format(result[self.i][0]))
        self.i += 1
        # #
        self.text_y_10.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_11.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_12.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_13.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_14.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_15.setText("{}".format(result[self.i][0]))
        self.i += 1


    def depression(self):
        self.pageup += 1
        self.main.setCurrentIndex(self.pageup)
        self.cur.execute("SELECT text FROM test_depression")
        result = self.cur.fetchall()
        self.conn.commit()
        self.i = 0

        self.text_y_1.setText("{}".format(result[self.i][0]))
        self.i += 1
        #
        self.text_y_2.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_3.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_4.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_5.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_6.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_7.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_y_8.setText("{}".format(result[self.i][0]))
        self.i += 1


    def next(self):
        self.pageup += 1
        self.main.setCurrentIndex(self.pageup)
    def happy4(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.q = 9
        if (self.h_19_1.isChecked() == True or self.h_19_2.isChecked() == True or self.h_19_3.isChecked() == True):
            self.a = 0
        if (self.h_20_1.isChecked() == True or self.h_20_2.isChecked() == True or self.h_20_3.isChecked() == True):
            self.b = 0
        if (self.h_21_1.isChecked() == True or self.h_21_2.isChecked() == True or self.h_21_3.isChecked() == True):
            self.c = 0
        if (self.h_22_1.isChecked() == True or self.h_22_2.isChecked() == True or self.h_22_3.isChecked() == True):
            self.d = 0
        if (self.h_23_1.isChecked() == True or self.h_23_2.isChecked() == True or self.h_23_3.isChecked() == True):
            self.e = 0
        if (self.h_24_1.isChecked() == True or self.h_24_2.isChecked() == True or self.h_24_3.isChecked() == True):
            self.f = 0
        if (self.h_25_1.isChecked() == True or self.h_25_2.isChecked() == True or self.h_25_3.isChecked() == True):
            self.g = 0
        if (self.h_26_1.isChecked() == True or self.h_26_2.isChecked() == True or self.h_26_3.isChecked() == True):
            self.h = 0
        if (self.h_27_1.isChecked() == True or self.h_27_2.isChecked() == True or self.h_27_3.isChecked() == True):
            self.q = 0
        if (self.a == self.b == self.c == self.d == self.e == self.f == self.g == self.h == self.q):
            if (self.h_19_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_19_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_19_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_20_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_20_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_20_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_21_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_21_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_21_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_22_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_22_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_22_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_23_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_23_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_23_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_24_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_24_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_24_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_25_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_25_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_25_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_26_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_26_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_26_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_27_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_27_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_27_3.isChecked() == True):
                self.happy_point += 2

            print(self.happy_point)
            print(self.i)
            self.pageup += 1
            self.main.setCurrentIndex(self.pageup)
            self.cur.execute("SELECT text FROM test_happy")
            result = self.cur.fetchall()
            self.conn.commit()
            self.text_h_28.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_29.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_30.setText("{}".format(result[self.i][0]))
        else:
            print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')
    def happy_end(self):
        self.a = 1
        self.b = 2
        self.c = 3
        if (self.h_28_1.isChecked() == True or self.h_28_2.isChecked() == True or self.h_28_3.isChecked() == True):
            self.a = 0
        if (self.h_29_1.isChecked() == True or self.h_29_2.isChecked() == True or self.h_29_3.isChecked() == True):
            self.b = 0
        if (self.h_30_1.isChecked() == True or self.h_30_2.isChecked() == True or self.h_30_3.isChecked() == True):
            self.c = 0
        if (self.a == self.b == self.c):
            if (self.h_28_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_28_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_28_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_29_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_29_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_29_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_30_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_30_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_30_3.isChecked() == True):
                self.happy_point += 0
            print(self.happy_point)
            print(self.i)
            if (self.happy_point >= 41):
                self.j_1.setText("당신의 점수는 {}점입니다.".format(self.happy_point))
                self.pageup += 1
                self.main.setCurrentIndex(self.pageup)
            elif(self.happy_point <= 40):
                self.j_3.setText("당신의 점수는 {}점입니다.".format(self.happy_point))
                self.pageup += 2
                self.main.setCurrentIndex(self.pageup)
            self.cur.execute("SELECT user_name FROM user")
            result1 = self.cur.fetchall()
            user_list = []

            for i in result1:
                user_list.append(i[0])
            # print(user_list1[0])
            # print(user_list)
            print(self.nickname)
            # print(user_list[0][0])
            if (self.nickname in user_list):
                print("update2")
                self.cur.execute(
                    "UPDATE user set happy = '{}' WHERE user_name = '{}'".format(self.happy_point, self.nickname))
                print("update")
                self.conn.commit()
            else:
                print("insert1")
                self.cur.execute("INSERT INTO user values('{}','{}','{}')".format(self.nickname, self.happy_point, 0))
                print("insert")
                self.conn.commit()
        else:
            print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')
    def happy3(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.q = 9
        if (self.h_10_1.isChecked() == True or self.h_10_2.isChecked() == True or self.h_10_3.isChecked() == True):
            self.a = 0
        if (self.h_11_1.isChecked() == True or self.h_11_2.isChecked() == True or self.h_11_3.isChecked() == True):
            self.b = 0
        if (self.h_12_1.isChecked() == True or self.h_12_2.isChecked() == True or self.h_12_3.isChecked() == True):
            self.c = 0
        if (self.h_13_1.isChecked() == True or self.h_13_2.isChecked() == True or self.h_13_3.isChecked() == True):
            self.d = 0
        if (self.h_14_1.isChecked() == True or self.h_14_2.isChecked() == True or self.h_14_3.isChecked() == True):
            self.e = 0
        if (self.h_15_1.isChecked() == True or self.h_15_2.isChecked() == True or self.h_15_3.isChecked() == True):
            self.f = 0
        if (self.h_16_1.isChecked() == True or self.h_16_2.isChecked() == True or self.h_16_3.isChecked() == True):
            self.g = 0
        if (self.h_17_1.isChecked() == True or self.h_17_2.isChecked() == True or self.h_17_3.isChecked() == True):
            self.h = 0
        if (self.h_18_1.isChecked() == True or self.h_18_2.isChecked() == True or self.h_18_3.isChecked() == True):
            self.q = 0
        if (self.a == self.b == self.c == self.d == self.e == self.f == self.g == self.h == self.q):
            if (self.h_10_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_10_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_10_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_11_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_11_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_11_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_12_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_12_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_12_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_13_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_13_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_13_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_14_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_14_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_14_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_15_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_15_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_15_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_16_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_16_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_16_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_17_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_17_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_17_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_18_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_18_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_18_3.isChecked() == True):
                self.happy_point += 0

            print(self.happy_point)
            print(self.i)
            self.pageup += 1
            self.main.setCurrentIndex(self.pageup)
            self.happy3page()
        else:
            print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')
    def happy3page(self):
        self.cur.execute("SELECT text FROM test_happy")
        result = self.cur.fetchall()
        self.main.setCurrentIndex(self.pageup)
        self.conn.commit()
        self.text_h_19.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_20.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_21.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_22.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_23.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_24.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_25.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_26.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_27.setText("{}".format(result[self.i][0]))
        self.i += 1

    def happy2(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.q = 9
        if (self.h_1_1.isChecked() == True or self.h_1_2.isChecked() == True or self.h_1_3.isChecked() == True):
            self.a = 0
        if (self.h_2_1.isChecked() == True or self.h_2_2.isChecked() == True or self.h_2_3.isChecked() == True):
            self.b = 0
        if (self.h_3_1.isChecked() == True or self.h_3_2.isChecked() == True or self.h_3_3.isChecked() == True):
            self.c = 0
        if (self.h_4_1.isChecked() == True or self.h_4_2.isChecked() == True or self.h_4_3.isChecked() == True):
            self.d = 0
        if (self.h_5_1.isChecked() == True or self.h_5_2.isChecked() == True or self.h_5_3.isChecked() == True):
            self.e = 0
        if (self.h_6_1.isChecked() == True or self.h_6_2.isChecked() == True or self.h_6_3.isChecked() == True):
            self.f = 0
        if (self.h_7_1.isChecked() == True or self.h_7_2.isChecked() == True or self.h_7_3.isChecked() == True):
            self.g = 0
        if (self.h_8_1.isChecked() == True or self.h_8_2.isChecked() == True or self.h_8_3.isChecked() == True):
            self.h = 0
        if (self.h_9_1.isChecked() == True or self.h_9_2.isChecked() == True or self.h_9_3.isChecked() == True):
            self.q = 0
        if (self.a == self.b == self.c == self.d == self.e == self.f == self.g == self.h == self.q):

            if (self.h_1_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_1_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_1_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_2_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_2_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_2_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_3_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_3_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_3_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_4_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_4_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_4_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_5_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_5_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_5_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_6_1.isChecked() == True):
                self.happy_point += 2
            elif (self.h_6_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_6_3.isChecked() == True):
                self.happy_point += 0
            if (self.h_7_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_7_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_7_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_8_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_8_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_8_3.isChecked() == True):
                self.happy_point += 2
            if (self.h_9_1.isChecked() == True):
                self.happy_point += 0
            elif (self.h_9_2.isChecked() == True):
                self.happy_point += 1
            elif (self.h_9_3.isChecked() == True):
                self.happy_point += 2

            print(self.happy_point)
            self.pageup += 1
            self.main.setCurrentIndex(self.pageup)
            self.happy2page()
        else:
            # print("ㅎㅇ")
            QMessageBox.critical(self, 'error', '문항을 전부 체크해주십시요.')
    def happy(self):

        self.nickname = self.name.toPlainText()
        if(len(self.nickname) < 3):
            QMessageBox.critical(self, 'error', '닉네임이 짧습니다.')
        else:
            self.name_1.setText("{}".format(self.nickname))
            self.name_2.setText("{}".format(self.nickname))
            self.name_3.setText("{}".format(self.nickname))
            self.name_4.setText("{}".format(self.nickname))
            self.name_5.setText("{}".format(self.nickname))
            self.name_6.setText("{}".format(self.nickname))

            self.cur.execute("SELECT text FROM test_happy")
            result = self.cur.fetchall()
            self.main.setCurrentIndex(self.pageup)
            self.conn.commit()

            self.text_h_1.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_2.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_3.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_4.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_5.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_6.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_7.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_8.setText("{}".format(result[self.i][0]))
            self.i += 1

            self.text_h_9.setText("{}".format(result[self.i][0]))
            self.i += 1
    def happy2page(self):
        self.cur.execute("SELECT text FROM test_happy")
        result = self.cur.fetchall()
        self.main.setCurrentIndex(self.pageup)
        self.conn.commit()
        self.text_h_10.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_11.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_12.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_13.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_14.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_15.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_16.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_17.setText("{}".format(result[self.i][0]))
        self.i += 1

        self.text_h_18.setText("{}".format(result[self.i][0]))
        self.i += 1

    wwd(self):
        mainWindow.close()
        self.cur.execute("SELECT * from user WHERE happy >=41")  # happy 41 이상 호출
        result = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy >= 41")  # depression 평균 호출
        result1 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result))
        happy = []
        for i in range(len(result)):
            happy.append(result[i][1])
        print(len(happy))
        print(result1[0][0])

        self.cur.execute("SELECT * from user WHERE happy < 41 and happy >= 30")  # happy 41 미만 30이상 호출
        result2 = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy < 41 and happy >= 30")  # depression 평균 호출
        result3 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result1))
        happy1 = []
        for i in range(len(result2)):
            happy1.append(result2[i][1])
        print(len(happy1))
        print(result3[0][0])

        self.cur.execute("SELECT * from user WHERE happy <=29")  # happy 29 이하 호출
        result4 = self.cur.fetchall()
        self.cur.execute("SELECT avg(depression) from user WHERE happy <=29")  # depression 평균 호출
        result5 = self.cur.fetchall()
        self.conn.commit()
        # print(len(result2))
        happy2 = []
        for i in range(len(result4)):
            happy2.append(result4[i][1])
        print(len(happy2))
        print(result5[0][0])

        mpl_fig = plt.figure()  # 그래프 창생성

        ax = mpl_fig.add_subplot(111)  # 그래프 창에 1x1 그리드의 첫번째 subplot 생성
        N = 3
        hp = (len(happy), len(happy1), len(happy2))
        de = (result1[0][0], result3[0][0], result5[0][0])

        ind = np.arange(N)
        width = 0.35  # 너비
        p1 = ax.bar(ind - 0.2, hp, width, color='blue')
        p2 = ax.bar(ind + 0.2, de, width, color='red')
        ax.set_title('happy&depression Test')
        ax.set_yticks(np.arange(0, 41, 5))
        ax.set_xticks(ind)
        ax.set_xticklabels(('60~40', '39~25', '24~0'))
        ax.legend(["happy", "depression"], loc=0)
        plt.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
