#!/usr/bin/python3
import keyword
# 第一个注释
"""
123
"""
print("Hello, Python!")  # 第二个注释
# 缩进表示代码块
if True:
    print("True")
else:
    print("False")
# 如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
totalList = ['item_one', 'item_two', 'item_three',
             'item_four', 'item_five']
# 关键字
print(keyword.kwlist)