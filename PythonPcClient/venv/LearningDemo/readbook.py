# print ("hello word")
# message='we will win'
# print(message.title())#大写首字母
# print(message.upper())#全部大写
# print(message.lower())#全部转换成小写
# language=' p y t h o n '
# print(language.strip())#除去字符全部空格
# print(language.lstrip())#除去字符头部空格
# print(language.rstrip())#除去字符末尾空格
# bicycles=['China','America','Englind']#列表
# bicycles.append('Japan')#为列表添加元
# print(bicycles[-1])#访问列表最后一元素
# bicycles.insert(0,'AcientChina')#插入元素
# print(bicycles[0])#访问列表第一个元素
# del bicycles[0]#del方法删除元素
# print(bicycles[0])
# print(bicycles.pop())#pop（）方法删除列表尾元素，并弹出该元素
# bicycles=['China','America','Englind']#列表
# print(bicycles.pop(0))#pop（*）方法删除列表任意位置元素，并弹出该元素
# bicycles=['China','America','Englind']#列表
# bicycles.remove('America')#remove()方法，删除任意元素
# print(bicycles)
# cars=['bwm','audi','toyota','subaru']
# cars.sort()#永久性按字母顺序排序
# cars.sort(reverse=True)
# print(sorted(cars))#sorted方法临时排序
# cars.reverse()#永久性倒序排列
# print(cars)
# print(len(cars))#获得列表的长度
# for car in cars:
# 	print(car)
# for value in range(1,5):#range函数生成一系列数字
# 	print(value)
# even_numbers=list(range(2,11,2))#使用list()和range()生成1-10之间的偶数
# print(even_numbers)
# print('MAX'+str(max(even_numbers))+'\t'+'MIN'+str(min(even_numbers))+'\t'
# +'SUM'+str(sum(even_numbers)))#使用最大值，最小值，求和函数
# squares = [values**2 for values in range(1,11)]#列表解析
# print(squares)
# players = ['charles','martina','michale','florence','eli']
# print(players[0:3])#生成切片78页
# 元组当中的元素是不能改变的，如果想要改变就只能重新定义远元组
# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())
# car = 'Audi'
# print(car.lower() == 'audi')#lower可以将字母全部转换成小写在进行比较，比较之间用and 和 or 进行连接
# print("audi" in cars)#可以直接输出元素是否在某个列表之中

# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")
#
# requested_toppings = ['10']
# if requested_toppings:#if 语句是可以直接判断列表当中是否为空的
#     print("列表不为空")
# alien_0 = {'color': 'green', 'points': 5,'name':'xiaomao'}#python当中的字典是以键值的形式来储存数据的
# print(alien_0)#可以直接打印字典的名字，也可打印列表当中的键值
# print(alien_0['points'])
# del alien_0['points']#删除字典当中的元素
# print(alien_0)
# alien_1 = {}#创建一个空字典
# for k,n in alien_0.items():
#     print("\nKey:"+k)
#     print('Value:'+n)
# favorite_languages = {
#  'jen': 'python，c,java',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  'admin': 'python,ruby'
#  }
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +", I see your favorite language is " +
#           favorite_languages[name].title() + "!")

# for name in sorted(favorite_languages.keys()):#按照顺序输出键
#     print(name.title()+",thank you for taking the poll")
# for language in favorite_languages.values():#遍历列表当中所有的值
#     print(language.title())

# for language in set(favorite_languages.values()):#使用集合遍历列表当中所有的值，不包含重复值
#     print(language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0,alien_1,alien_2]#列表嵌套字典，然后可以输出，也可以利用这一点循环生成相同的字典对象
# print(aliens)

# favorite_languages = {#在字典当中嵌套列表
#  'jen': ['python，c,java'],
#  'sarah': ['c'],
#  'edward': ['ruby'],
#  'phil': ['python'],
#  'admin': ['python,ruby']
#  }
#
# for name,languages in favorite_languages.items():
#     print("\n"+name.title()+"'s favorite languages are:")
#     for language in languages:
#         print("\t"+language.title())#将其分别输出，用到了for的嵌套

# message = input("Tell me something,and I will repeat it back to you:")
# print(message)#等待用户输入的方法，python2.7当中使用raw_input()来获取输入

# height = input("How tall are you,in inches? ")
# height = int(height)#强行将str类型的数字字符转换成整数的方法
# if height >=36:
#     print("\nYou're tall enough to ride")#132

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)使用remove将列表当中指定的元素除移

# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhich is your name? ")
#     response = input("\nWhich mountain would you like to climb someday? ")
#     responses[name] = response
#     repeat = input("\nWould you like to let another person respond?(yes/no) ")
#     if repeat == ('no'):
#         polling_active = False
# print('\n---Poll Results')
# for name,response in responses.items():
#     print(name + "would like to climb "+response + ".")

# def describ_pet (animal_type,pet_name = 'hello'):#函数参数可以有默认值
#     """显示宠物信息"""
#     print("\nI have a "+animal_type+".")
#     print("\nMy "+animal_type + "'s name is "+pet_name.title()+".")
# describ_pet('hamster','harry')#位置实参
# describ_pet(pet_name = 'harry',animal_type='hamster')#关键字实参，位置可以调换

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# unprinted_designs_1 = unprinted_designs[:]#创建一个副本，使用副本传参，可以避免实参被函数改动
#
# def make_pizza(*toppings):#可以传递任意数量的实参,会被封装到一个元组当中
#     #  """打印顾客点的所有配料"""
#     print(toppings)
# make_pizza('peoperoni')
# make_pizza('hihiihi','whefhwh','jslfjof')
# def make_pizza_1(size,*toppings):#位置实参和任意数量实参相结合，任意数量实参必须放在最后
#     print('\nMaking a '+str(size)+'-inch pizza with the following toppings: ')
#     for topoing in toppings:
#         print("- "+topoing)
# make_pizza_1(15,'zhou','liang','hao')

#import关键字可以导入模块，并且还可以仅仅导入某个模块的某一个函数，还可以在导入是用as给这个导入的函数重新命名
#import pizza#导入整个模块，然后以模块名.函数名的方式来引用模块当中的函数
#from pizza import make_pizza#仅仅导入一个函数
#from pizza import make_pizza as mp给导入的函数指定别名，当函数名冲突的时候可以这么做
#import pizza as p#导入是给模块指定别名
#from pizza import *导入模块当中的所有函数，最好不要这样做因为容易引起函数名的大规模冲突

#首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类。

# class Dog(object):#创建一个类，类的名字第一个字母默认要大写，在python2.7当中，定义类要在括号当中加上object
#     """创建第一个python类"""
#     def __init__(self, name, age):
#         """初始化类的属性"""
#         self.name = name
#         self.age = age
#     def sit(self):#类当中的方法，调用时和java一样
#         print(self.name.tiele() + " is now sitting!")
#     def roll_over(self):
#         print(self.name.tiele() + " rolled over!")
# my_dog = Dog('wille',6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# class BigDog(Dog):
#     def __init__(self,name,age):#类的继承
#         super().__init__(name,age)#170
#
# from collections import OrderedDict#导入有序字典类，从标准库当中导入
# favorite_languages = OrderedDict()
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'
# for name,language in favorite_languages.items():
#     print(name.title()+"'s favorite language is "+language.title())
# favorite_languages1 = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
# for name,language in favorite_languages1.items():
#     print(name.title()+"'s favorite language is "+language.title())
# favorite_languages2 = {}
# favorite_languages2['jen'] = 'python'
# favorite_languages2['sarah'] = 'c'
# favorite_languages2['edward'] = 'ruby'
# favorite_languages2['phil'] = 'python'
# for name,language in favorite_languages2.items():
#     print(name.title()+"'s favorite language is "+language.title())

# with open('pi_digits.txt') as file_object:
# #     contents = file_object.read()
# #     print(contents.rstrip())#使用rstrip方法删除read到达文件末尾时返回的空字符串
# # with open('pi_digits.txt') as file_object:
# #     i = 1
# #     for line in file_object:
# #         print(line.rstrip()+"---行数"+str(i))
# #         i=i+1
# # with open('pi_digits.txt') as file_object:
# #     lines = file_object.readlines()#将文件当中每一行的数据输出道列表当中
# # pi_string = ''
# # for line in lines:
# #     pi_string +=line.strip()#删除每一行左边的空格
# # print(pi_string)
# # print(len(pi_string))

# with open('filename.txt','w') as file_oject:#以写的形式打开了文件，如果文件不存在，会自动创建，如果存在之前的内容会被清空
#     file_oject.write("你好这是第一行输出的内容！\n")
#     file_oject.write("这是第二行！\n")

# with open("filename.txt",'a') as file_object:#以添加的形式打开文件
#     file_object.write("这是添加的一行，之前的内容不会被清除")

# try:#抛出异常避免程序崩溃
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")#如果这里写pass，出现异常就会被略过

# title = "Alice in Wonderland"#将一句英语句子以空格为分隔符拆分成为英语单词
# print(title.split())
# print(len(title.split()))

# import json
# numbers = [2,3,5,7,11,13]
# filename = 'numbers.json'
# with open(filename,'w') as f_obj:
#     json.dump(numbers,f_obj)