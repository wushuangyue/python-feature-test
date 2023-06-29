'''
Author: wushuangyue 121999194+wushuangyue@users.noreply.github.com
Date: 2023-06-29 21:08:26
LastEditors: wushuangyue 121999194+wushuangyue@users.noreply.github.com
LastEditTime: 2023-06-29 21:10:02
FilePath: \python-feature-test\statement_loop.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/env python3
 
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

flag = 1
 
while (flag): print ('欢迎访问菜鸟教程!')
 
print ("Good bye!")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

word = 'runoob'
 
for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")