'''
Author: wushuangyue 121999194+wushuangyue@users.noreply.github.com
Date: 2023-06-29 20:53:12
LastEditors: wushuangyue 121999194+wushuangyue@users.noreply.github.com
LastEditTime: 2023-06-29 20:53:41
FilePath: \python-feature-test\datatype_Dictionary.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#!/usr/bin/python3

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值