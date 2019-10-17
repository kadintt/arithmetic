#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import smtplib
from email.header import Header
import pymysql.cursors
import xlsxwriter
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import datetime
from DBUtils.PooledDB import PooledDB
import decimal
import time

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
    # 创建数据库链接池  5 为连接池里的最少连接数
    pool = PooledDB(pymysql, 5, host='121.196.232.93', user='readonly', passwd='J8mRjfWeBwNnQi2', db='simeitol_uc', port=3306)
    pool = PooledDB(pymysql, 5, host='121.196.232.93', user='readonly', passwd='J8mRjfWeBwNnQi2', db='zmt_shop', port=3306)

    conn = pool.connection()
    cursor = conn.cursor()
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday

    cB = yesterday.strftime('%Y-%m-%d 00:00:00')
    cE = yesterday.strftime('%Y-%m-%d 23:59:59')
    beginT = str(int(time.mktime(time.strptime(cB, '%Y-%m-%d %H:%M:%S')) * 1000))
    endT = str(int(time.mktime(time.strptime(cE, '%Y-%m-%d %H:%M:%S')) * 1000))
    print(beginT, endT)
    s1 = "SELECT u.nickName, \
 i.goodsName, \
 m.saleOrderStatus, \
 m.specifications, \
 m.activityPrice, \
 m.grouponGoodsItemId, \
 from_unixtime( \
  m.createTime / 1000, \
  '%Y-%m-%d %H:%i:%S' \
 ) formatCreateTime \
FROM \
 meetao_pt_groupon_activity_order_relation m \
LEFT JOIN simeitol_uc.simeitol_user u ON m.userId = u.userId \
LEFT JOIN meetao_sales_order_detail d ON m.saleOrderId = d.orderId \
LEFT JOIN meetao_pt_groupon_activity_goods_item g ON g.id = m.grouponGoodsItemId \
LEFT JOIN meetao_goods_items i ON g.goodsCode = i.goodsCode WHERE "

    s5 = " d.createTime > "
    s3 = " AND d.createTime < "
    sql = s1 + s5 + beginT + s3 + endT

    print(sql)
    # 执行sql
    cursor.execute(sql)
    # 读取查询结果
    data = cursor.fetchall()

    print(data)

    itemList = []
    for item in data:
        # item.append(timestr)
        strList = []
        for i in item:
            strList.append(i)
        itemList.append(strList)

    for item in itemList:
        time1 = item[-3]
        # 将Decimal 转成str
        time1 = str(decimal.Decimal(time1).quantize(decimal.Decimal('0.00')))
        print(time1)
        # 重新赋值
        item[-3] = time1

    print(itemList)

    titleList = ['昵称', '商品名称', '订单状态', '商品规格', '商品价格', '拼团商品id', '创建时间']

    filePatth = save(titleList, itemList)
    # 关闭
    cursor.close()
    conn.close()

    #发送邮件
    send = SendMail()
    send.sendMail("昨日数据汇总", "今天天气不错", filePatth)
