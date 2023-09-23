# name = "akbar"
# #print(name.count("a"))
# #print(name.upper())
# #print(name.find("r"))
# #print(name.replace("r", "z"))
# print(name * 3)

# name = input("what is your name")
# age = int(input("how old are you"))
# height = float(input("how toll are you"))
#
# print("your name is :" + str(name))
# print("your age is :" + str(age))
# print("your height is :" + str(height))

#index slicing , slice function
# name = "22akbar11"
# print(name[2:7])
# slice1 = slice(2, -2)
# print(name[slice1])

#if statments
# age = int(input("enter your age:"))
# if age == 100:
#     print("your centuray")
# elif age >= 18:
#     print("You are adult")
# elif age < 0:
#     print("you are not born")
# else:
#     print("you are baby")

#logical operators
# temp = int(input("enter the weather condition"))
# if temp >= 0 and temp <= 30:
#     print("weather is good")
# elif temp < 0 or temp > 30:
#     print("weather is not good")

#while loop
# name = None
# while not name:
#     name = input("enter your name")
#
# print("hello")

#for loop
# for i in range(10, 20 + 1, 2):
#     print(i)


# for i in  "akbar":
#     print(i)

#nested loops
# row = int(input("enter how many row:"))
# column = int(input("how many column:"))
# symbol = input("which symbol:")
#
# for i in range(row):
#     for j in range(column):
#         print(symbol, end=" ")
#     print()

#break, continue,pass
# for i in range(1, 30):
#     if i == 13:
#         pass
#     else:
#         print(i)

#    list
#          food = ["pizza", "apple", "banana"]
#           food[1] = "sushi"
#           print(food)

#           for i in food:
#               print(i)
#          num = [3, 5, 3, 1, 9, 19]
#          list1 = ["akku", "basi", "lalu"]
#          rint(list1 + num)
#          food.append("papaya")
#          food2 = food.copy()
#          num.sort()
#          num.remove(9)
#          num.pop()
#          num.count(3)
#          num.insert(0, "akku")
#          num.clear()
#          num.remove()
#          print(num)

#print(food)
#print(food2)

# 2D list
# class Animal1:
#     def wild_animal(self, n):
#         self.name = n
#     def print_name(self):
#         print(self.name)
#
# obj1 = Animal1()
# obj1.wild_animal("akku")
# obj1.print_name()
# obj2 = Animal1()
# obj2.wild_animal("kukku")
# obj2.print_name()

# constructor
# class MyClass:
#     year = 2023
#     def __init__(self, name, age, place):
#         self.name = name
#         self.age = age
#         self.place = place
#     def add_age(self):
#         self.age = self.age+1
#     def re_locate(self, place):
#         self.place = place
#     def displa(self):
#         print("year : ", MyClass.year)
#         print("name : ", self.name)
#         print("age : ", self.age)
#         print("palce : ", self.place)
#     @classmethod
#     def add_year(cls):
#         cls.year = cls.year+1
#
# obj1 = MyClass("akku", 25, "ekd")
# obj1.displa()
# print("__________________________")
# obj1.add_age()
# obj1.add_year()
# obj1.re_locate("Goa")
# obj1.displa()

#2D list
# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# list3 = [list1 , list2]
# print(list3[1][4])

#inheritance
# class BaseClass:
#     def firstOne(self):
#         print("hello")
#
# class SubClass(BaseClass):
#     def SecondOne(self):
#         print("Akbar")
#
# obj1 = BaseClass()
# obj1.firstOne()
#
# obj2 = SubClass()
# obj2.firstOne()
# obj2.SecondOne()

# 2nd Example
# class A:
#     num1 = int(input("Enter first number"))
#     num2 = int(input("Enter second number"))
#     def add(self):
#         print("Addition", self.num1 + self.num2)
#     def sub(self):
#         print("Subtraction", self.num1 - self.num2)
#
# class B(A):
#     def mul(self):
#         print("Multiplication", self.num1 * self.num2)
#     def div(self):
#         print("Division", self.num1 / self.num2)
#
# obj1 = A()
# obj1.add()
# obj1.sub()
#
# obj2 = B()
# obj2.add()
# obj2.sub()
# obj2.mul()
# obj2.div()

#multi level inheritance
# class Father:
#     surname = "panthakkan"
#
# class son1(Father):
#     def display(self):
#         print("Akbar", self.surname)
#
# class son2 (son1):
#     def show(self):
#         print("Ayisha", self.surname)
#
# s1 = son1()
# s1.display()
# s2 = son2()
# s2.show()
#

#multiple inheritance
# class Backend:
#     B = "Mongo_db"
#     def backend_work(self):
#         print("Backend creating :", self.B)
# class Frontent:
#     F = "Html&Css"
#     def frontent_work(self):
#         print("Frontent created :", self.F)
#
# class Website(Backend, Frontent):
#     print("website created successfully")
#
# w = Website()
# w.backend_work()
# w.frontent_work()


#a = []

# def get_array():
#     s = int(input("Enter size: "))
#     for i in range(s):
#         value = int(input("Enter value: "))
#         a.append(value)
#
# def display_array():
#     print("Array is:", a)
#
# get_array()
# display_array()

#function example


#function return value example

# def function1():
#     n = 10 + 20
#     return n
#
# print(function1())
#
# def function1(name):
#     print("hai", name)
#
# function1("akku")

# class Father:
#     surname = "panthakan"
#     def display(self):
#         print("my surname is :", self.surname)
# class Son1(Father):
#     def show(self):
#         print("My name is akbar ali ", self.surname)
# class Son2(Father):
#     def show(self):
#         print("My name is Ayisha ", self.surname)
#
# f = Father()
# f.display()
# print("___________________")
# s1 = Son1()
# s1.show()
# print("___________________")
# s2 = Son2()
# s2.show()
#


# def upper_dec(funi):
#     def wrapper(name):
#         result = funi(name)
#         return result.upper()
#     return wrapper
# @upper_dec
# def function1(name):
#     return "hello dear" + name
#
# print(function1(" mammootty"))
#
#
# def upper_dec(fun):
#     def wrapper():
#         result = fun()
#         return result.upper()
#     return wrapper
#
# @upper_dec
# def function1():
#     return "hello akbar"
#
# print(function1())
#
# class Father:
#     surname = "panthakkan"
#
# class son1(Father):
#     def display(self):
#         print("Akbar", self.surname)
#
# s1 = son1()
# s1.display()
#
#
#
# class Father:
#     num1 = int(input("enter first number"))
#     num2 = int(input("enter second number"))
#     def add(self):
#         print("addition :", self.num1 + self.num2)
# class sub1(Father):
#     def sub(self):
#         print("Subtraction :", self.num1 - self.num2)
# class sub2(sub1):
#     def mul(self):
#         print("Multiplication :", self.num1 * self.num2)
#
# f = Father()
# f.add()
# print("_______________")
# s1 = sub1()
# s1.add()
# s1.sub()
# print("_______________")
# s2 = sub2()
# s2.add()
# s2.sub()
# s2.mul()
#
# class backend:
#     b = "oracle"
#     def display(self):
#         print("backend :", self.b)
# class frotent:
#     c = "html"
#     def show(self):
#         print("Frotent :", self.c)
# class web(backend, frotent):
#     def open(self):
#         print("Website created :", self.b, self.c)
#
#
# w = web()
# w.open()
# w.display()
# w.show()
#
# class MyClass:
#     def __init__(self, name, place, age):
#         self.name = name
#         self.place = place
#         self.age = age
#
#     def display(self):
#         print("My name is :", self.name,"place :", self.place, "Age :", self.age)
#
# obj1 = MyClass("Akku", "edarikode", 25)
# obj1.display()
#
#
# x = lambda a, b: a*b
# print(x(10, 20))
#
# class A:
#     def show(self):
#         print("welcome")
#     def show(self, firstname=''):
#         print("welcome", firstname)
#     def show(self, firstname='', lastname=''):
#         print("welcome", firstname, lastname)
#
#
# o = A()
# o.show()
# o.show("akbar")
# o.show("akbar", "ali")
#
#
# class A:
#     _a=10 #protected
#     __b=20 #private
#     def display(self):
#         print("a  :", self._a)
#         print("b  :", self.__b)
#
# o = A()
# o.display()
# print("a:", A._a)
# print("b =", A.__b)

# a = [i+i for i in range(10)]
# print(a)
dict = {
    "name" : "akku",
    "age" : 25,
    "phone" : 758752
}

print(dict.get("hai"))

set1 = {1, "hello", 5, 4, 9}
print(set1)








