'''
Author: wushuangyue 121999194+wushuangyue@users.noreply.github.com
Date: 2023-06-29 21:24:35
LastEditors: wushuangyue 121999194+wushuangyue@users.noreply.github.com
LastEditTime: 2023-06-29 21:25:15
FilePath: \python-feature-test\oop_class_overriding.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/python3
 
class Parent:        # 定义父类
   def myMethod(self):
      print ('调用父类方法')
 
class Child(Parent): # 定义子类
   def myMethod(self):
      print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法