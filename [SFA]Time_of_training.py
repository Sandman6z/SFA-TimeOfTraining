#!/usr/bin/python
# -*- coding: UTF-8 -*-

###################################################################
# 6月5日-6月11日
# B757#1
# 计划训练时间68小时，实际训练时间67小时40分钟，可利用率99.5%。
# 发生故障1条，解决1条，遗留0条。

# B757#3
# 计划训练时间62小时，实际训练时间62小时，可利用率100%。
# 发生故障1条，解决1条，遗留0条。


# 本周（6月07日-6月13日）模拟机运营数据统计：
# 1）1# 可用112时间小时，训练时间68小时，利用率61%；
# 2）3# 可用时间112小时，训练时间62小时，利用率55%。
# 平均利用率：58%
###################################################################
import datetime
import time
import os

# 获取当前日期
# today = datetime.date.today()
# month = datetime.datetime.now().month
# day = datetime.datetime.now().day


# 获取当前是周几(0-6,0代表周一)
weekday = datetime.datetime.now().weekday()

# 标题
print("\n{0:~^30}\n".format("超low手动训练数据生成"))

hours2_1 = float(input("请输入B757 #1 本周 2小时 训练数:"))
hours4_1 = int(input("请输入B757 #1 本周 4小时 训练数:"))
delay_1 = float(input("请输入B757 #1 本周延误小时数:"))
hours2_3 = float(input("\n请输入B757 #3 本周 2小时 训练数:"))
hours4_3 = int(input("请输入B757 #3 本周 4小时 训练数:"))
delay_3 = float(input("请输入B757 #3本周延误小时数:"))
print("\n\n")

plan_time_1 = hours2_1 * 2 + hours4_1 * 4
plan_time_3 = (hours2_3 * 2) + (hours4_3 * 4)

trn_time_1 = plan_time_1 - delay_1
trn_time_3 = plan_time_3 - delay_3

percent_1 = trn_time_1 / plan_time_1
percent_3 = trn_time_3 / plan_time_3

# def get_current_week():
#     monday, sunday = datetime.date.today(), datetime.date.today()
#     one_day = datetime.timedelta(days=1)
#     while monday.weekday() != 0:
#         monday -= one_day
#     while sunday.weekday() != 6:
#         sunday += one_day
	
#     return monday, sunday
#     # 返回时间字符串
#     #  return datetime.datetime.strftime(monday, "%Y/%m/%d") + ' 00:00:00+08:00', datetime.datetime.strftime(sunday, "%Y/%m/%d")+ ' 23:59:59+08:00'  

def get_current_monday():
    monday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while monday.weekday() != 0:
        monday -= one_day
	
    return datetime.datetime.strftime(monday, "%m月%d日")

def get_current_sunday():
    sunday = datetime.date.today()
    one_day = datetime.timedelta(days=1)
    while sunday.weekday() != 6:
        sunday += one_day
	
    return datetime.datetime.strftime(sunday, "%m月%d日")

#输出内容
print(time.strftime("%Y年%m月%d日"))
print("本周({}-{}) 模拟机运营数据统计：".format(get_current_monday(), get_current_sunday()))
print("1）B757#1 可用时间{}小时，训练时间{}小时，利用率{:.2%}；".format(plan_time_1, trn_time_1, percent_1))
print("2）B757#3 可用时间{}小时，训练时间{}小时，利用率{:.2%}。".format(plan_time_3, trn_time_3, percent_3))
print("平均利用率：{:.2%}".format((percent_1 + percent_3) / 2))
os.system('pause')
