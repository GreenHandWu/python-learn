# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


# Number（数字）
# int、float、bool、complex（复数）

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
print(isinstance(a, int))

# Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# 使用del语句删除一些对象引用
# del var
# del var_a, var_b

# 计算
# + 加法
# - 减法
# * 乘法
# / 除法，得到一个浮点数
# //除法，得到一个整数
# % 取余
# ** 乘方

# 一个变量可以通过赋值指向不同类型的对象。
# 在混合计算时，Python会把整型转换成为浮点数。

# String（字符串）
# 略


# List（列表）
# 索引值以 0 为开始值，-1 为从末尾的开始位置。

# 加号 + 是列表连接运算符，星号 * 是重复操作
# (左闭右开)
my_list = ['abcd', 786, 2.23, 'runoob', 70.2]
tiny_list = [123, 'runoob']

print(my_list)  # 输出完整列表
print(my_list[0])  # 输出列表第一个元素
print(my_list[1:3])  # 从第二个开始输出到第三个元素
print(my_list[2:])  # 输出从第三个元素开始的所有元素
print(tiny_list * 2)  # 输出两次列表
print(my_list + tiny_list)  # 连接列表


# 以索引为列  [索引] 和 [索引:索引:步长] 的区别
# demo[索引] 取出的原列表中索引对应的元素
# demo[索引:索引:步长] 切片得到的是一个新列表
demo = [1,2,3,4,5,6]

new_demo = demo[1::2]  # 2 就是步长 意思是从索引为 1 的元素开始 每隔2个元素取一次元素
new_demo1 = [2,4,6]

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。

my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tiny_tuple = (123, 'runoob')

print(my_tuple)  # 输出完整元组
print(my_tuple[0])  # 输出元组的第一个元素
print(my_tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(my_tuple[2:])  # 输出从第三个元素开始的所有元素
print(tiny_tuple * 2)  # 输出两次元组
print(my_tuple + tiny_tuple)  # 连接元组

