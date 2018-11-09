# coding=utf-8



# 模拟类
class Employee:
    '所有员工的基类，定义类属性'
    empCount = 0
    # 定义类属性方法
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # Employee.empCount += 1
        Employee.empCount = Employee.empCount + 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


# 创建 Employee 类的第一个对象
emp1 = Employee("Zara", 2000)
# 创建 Employee 类的第二个对象
emp2 = Employee("Manni", 5000)


emp1.displayCount()
emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount

