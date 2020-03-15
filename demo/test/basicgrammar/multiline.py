# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item_one = 1
item_two = 1
item_three = 1
total = item_one + \
        item_two + \
        item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total1 = ['item_one', 'item_two', 'item_three',
          'item_four', 'item_five']
