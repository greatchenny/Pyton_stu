# -*- coding: UTF-8 -*-

# coding=utf_8
# 定义类
# 定义类属性，变量赋值
# 定义类方法，函数，行为
# 类的实例化，定义对象名称，且给对象赋值，比如：张三，（姓名，工资）
# 调用类，叫XX干XX obj.方法&行为
# class keniu_staff:
#     # 定义类属性，变量赋值
#
#     # 定义类方法，函数，行为
#         # 初始化
#     def __int__(self, name, slary):
#         self.name = name
#         self.slary = slary
#         keniu_staff.empCount += 1
#
#     #def staff_cont(self):
#     #    print This is keniu keniu_staff.empCount
#
#     def staff_all(self):
#         print "name*"
#
#
#
# # 类的实例化，定义对象名称，且给对象赋值，比如：张三，（姓名，工资）
# chen = keniu_staff("chen", 9082)
# chen.staff_all()

class keniu_staff:
    empCount = 0
    # 定义类属性方法
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        keniu_staff.empCount += 1

    def staff_all(self):
        print "name:", self.name, "\n", "salary:", self.salary, "\n", "总人数：", keniu_staff.empCount

chen = keniu_staff("张三", 40444)
chen.name = "马马"
liu = keniu_staff("李四", 3323)
chen.staff_all()
liu.staff_all()
getattr(liu,'name')
setattr(chen, 'age', 18)

print getattr(liu, 'name')

name = chen.__dict__

import json
print json.dumps(name, ensure_ascii=False, encoding='UTF-8')


class father():
    chengji = 89
    url = "www.baidu.com"
    def name(self):
        print "This is a fater"

print father.__dict__

pin = father()
pin.name()
