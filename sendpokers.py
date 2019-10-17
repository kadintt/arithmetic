#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import smtplib
from email.header import Header
import MySQLdb
import pymysql.cursors
import xlsxwriter
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import datetime


class Card():
    def __init__(self, cardName, cardValue):
        self.cardName = cardName
        self.cardValue = cardValue



if __name__ == '__main__':
    connect = pymysql.Connect("47.94.142.174", "db_admin", "htv~@GoPFNBw4gXs=-3", "db_alisvo", charset='utf8')

    # 创建游标
    # cursor = db.cursor()
    cursor = connect.cursor()

    sql = "SELECT * FROM t_cards;"


    # 执行sql
    cursor.execute(sql)
    # 读取查询结果
    data = cursor.fetchall()
    print(data)
    cardList = []
    for item in data:
        name = item[1] + ("" if item[2] == "X" or item[2] == "D" else item[2])
        # name = item[1] + (item[2] if item[2] != 'X' or item[2] != 'D' else '')
        value = item[-1]
        card = Card(name, value)
        cardList.append(card)


    for cardItem in cardList:
        print(cardItem.cardName)
        print(cardItem.cardValue)
