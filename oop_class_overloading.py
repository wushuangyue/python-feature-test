'''
Author: wushuangyue 121999194+wushuangyue@users.noreply.github.com
Date: 2023-06-29 21:28:27
LastEditors: wushuangyue 121999194+wushuangyue@users.noreply.github.com
LastEditTime: 2023-06-29 21:28:54
FilePath: \python-feature-test\oop_class_overloading.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/python3
 
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b
 
   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)
 
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)