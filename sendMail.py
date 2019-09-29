#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import smtplib
from email.header import Header
import MySQLdb
import xlsxwriter
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart


class SendMail(object):

    def __init__(self):
        self.sender = '826198421@qq.com'
        self.receivers = ['quchao@simeitol.com']
        # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.smtpObj = smtplib.SMTP_SSL()
        self.smtpObj.connect('smtp.qq.com', 465)
        self.smtpObj.login(self.sender, 'gmcpbbbfggxcbbef')
        pass

    def sendMail(self, subject='', sendText='', filePath=''):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # self.message = MIMEText(sendText, 'plain', 'utf-8')
        self.message = MIMEMultipart()

        self.message['From'] = Header("占星师", 'utf-8')  # 发送者
        self.message['To'] = Header("小zz", 'utf-8')  # 接收者
        self.message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))
        attach = MIMEApplication(open(filePath, 'rb').read(), 'utf-8')
        attach.add_header('Content-Disposition', 'attachment', filename='数据汇总.xlsx',)
        self.message.attach(attach)

        if len(subject) > 0:
            self.subject = subject
        else:
            self.subject = 'Python SMTP 数据问题报告'
        self.message['Subject'] = Header(self.subject, 'utf-8')
        try:
            self.smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            self.smtpObj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException as e:
            print(e)
            print("Error: 无法发送邮件")

    # 'ENGINE': 'django.db.backends.mysql',
    # 'NAME': 'TestData',
    # 'USER': 'root',
    # 'HOST':'39.98.88.168',
    # 'PASSWORD': 'root',
    # 'PORT':'3306',

def save(titleList, itemList):
    name = "星座运势.xlsx"  # 要保存的文件名
    ws = xlsxwriter.Workbook(name)
    w = ws.add_worksheet('每日运势')
    excel_row = 1
    for i,index in enumerate(titleList):
        w.write(0, i, index)

    for i, index in enumerate(itemList):
        for j, item in enumerate(index):
            w.write(i+1, j, item)
    ws.close()
    return name

if __name__ == '__main__':
    #    建立连接               域名ip         账户    密码     库名
    db = MySQLdb.connect("39.98.88.168", "root", "root", "TestData", charset='utf8')
    # 创建游标
    cursor = db.cursor()

    sql = "SELECT * FROM ConstellationFortune WHERE Date = '2019年9月29日'"

    # 执行sql
    cursor.execute(sql)
    # 读取查询结果
    data = cursor.fetchall()

    sql1 = "SELECT Download_column FROM download_mysql WHERE Download_table = '星座运势'"
    cursor.execute(sql1)

    sqlTitle = cursor.fetchall()
    # 打印
    itemList = []
    for item in data:
        print(item)
        itemList.append(item[:-1])
    # print(type(sqlTitle))
    titleList = []
    for item in sqlTitle:
        print(item[0])
        titleList.append(item[0])
    filePatth = save(titleList, itemList)
    # 关闭
    cursor.close()
    db.close()

    send = SendMail()
    send.sendMail("每日星座运势", "今天天气不错", filePatth)