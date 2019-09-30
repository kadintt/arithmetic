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

class SendMail(object):

    def __init__(self):
        self.sender = '826198421@qq.com'
        self.receivers = ['yuzhongcheng@simeitol.com', 'zhangyating@simeitol.com']
        # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        self.smtpObj = smtplib.SMTP_SSL()
        self.smtpObj.connect('smtp.qq.com', 465)
        self.smtpObj.login(self.sender, 'gmcpbbbfggxcbbef')
        pass

    def sendMail(self, subject='', sendText='', filePath=''):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        # self.message = MIMEText(sendText, 'plain', 'utf-8')
        self.message = MIMEMultipart()

        self.message['From'] = Header("曲超", 'utf-8')  # 发送者
        self.message['To'] = Header("于忠诚", 'utf-8')  # 接收者
        self.message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))
        attach = MIMEApplication(open(filePath, 'rb').read(), 'utf-8')
        attach.add_header('Content-Disposition', 'attachment', filename='testData.xlsx',)
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

def save(titleList, itemList):
    name = "昨日数据.xlsx"  # 要保存的文件名
    ws = xlsxwriter.Workbook(name)
    w = ws.add_worksheet('昨日数据')
    excel_row = 1
    for i, index in enumerate(titleList):
        w.write(0, i, index)

    for i, index in enumerate(itemList):
        for j, item in enumerate(index):
            w.write(i+1, j, item)
    ws.close()
    return name

if __name__ == '__main__':
    # 生产数据库：地址：121.196.232.93    账户： readonly     密码 ： J8mRjfWeBwNnQi2
    #    建立连接               域名ip         账户    密码     库名
    # db = MySQLdb.connect("39.98.88.168", "root", "root", "TestData", charset='utf8')
    # db = MySQLdb.connect("121.196.232.93", "readonly", "J8mRjfWeBwNnQi2", "simeitol_uc" , charset='utf8')
    connect = pymysql.Connect("121.196.232.93", "readonly", "J8mRjfWeBwNnQi2", "simeitol_uc" , charset='utf8')

    # 创建游标
    # cursor = db.cursor()
    cursor = connect.cursor()

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print(type(yesterday))
    s1 = "SELECT nickName,phone,userSource,createTime FROM simeitol_user WHERE createTime > "
    s2 = yesterday.strftime('%Y-%m-%d 00:00:00')
    s3 = " AND createTime < "
    s4 = yesterday.strftime('%Y-%m-%d 23:59:59')
    print(s2, s4)
    sql = s1 + "'" + s2 + "'" + s3 + "'" + s4 + "'"

    print(sql)
    # 执行sql
    cursor.execute(sql)
    # 读取查询结果
    data = cursor.fetchall()
    # sql1 = "SELECT Download_column FROM download_mysql WHERE Download_table = '星座运势'"
    # cursor.execute(sql1)
    #
    # sqlTitle = cursor.fetchall()
    #
    # # 打印
    itemList = []
    for item in data:
        # item.append(timestr)
        strList = []
        for i in item:
            strList.append(i)
        itemList.append(strList)


    for item in itemList:
        time1 = item[-1]
        item.pop()
        timestr = time1.strftime('%Y-%m-%d %H:%M:%S')
        item.append(timestr)

    print(itemList)
    titleList = ['用户昵称', '电话', '渠道', '创建时间']

    filePatth = save(titleList, itemList)
    # 关闭
    # cursor.close()
    connect.commit()
    # 发送邮件
    # send = SendMail()
    # send.sendMail("昨日数据汇总", "今天天气不错", filePatth)