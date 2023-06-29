'''
Author: wushuangyue 121999194+wushuangyue@users.noreply.github.com
Date: 2023-06-29 21:07:38
LastEditors: wushuangyue 121999194+wushuangyue@users.noreply.github.com
LastEditTime: 2023-06-29 21:08:02
FilePath: \python-feature-test\statement_match.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(http_error(400))