#-------------------------7.1. Fancier Output Formatting-----------------------------------------
yes_votes = 42_572_654#数字中使用 _ 作为分隔符，提高可读性，不影响数值。编译时会自动忽略 _，等同于 42572654。
total_votes = 85_705_149#t同上
percentage = yes_votes / total_votes
#: 是 ​格式说明符，
# - 表示左对齐，9 表示总宽度为 9 字符。yes_votes 是数字，会先转换为字符串再对齐。
#2.2%的第一个2是​最小总宽度，表示整个字段（包括数字和 % 符号）至少占 2 字符宽度。
# 但 ​由于百分比数值通常超过 2 字符宽度，这个参数在此场景下 ​实际会被忽略。
# .2 ​仅控制小数点后的位数，与整数部分无关。
# %将小数转换为百分比格式（自动乘以 100，并添加 % 符号）
print("{:-9} YES votes  {:2.2%}".format(yes_votes, percentage))
print(f"{yes_votes:-9} YES votes  {percentage:2.2%}")#同上

# repr() or str() functions.
s="hello world!\n"
print(str(s))#hello world!<newLine>
print(repr(s))#adds string quotes and backslashes:'hello world!\n'

#--------------------------------7.1.1. Formatted String Literals------------------------------
#An optional format specifier allows greater control over how the value is formatted. 
import math
print(f"pi≈{math.pi:.3f}")#3.1415->3.142

# columns line up
tables={'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,tel in tables.items():
    print(f"{name:10}==>{tel:10}")#字符串默认左对齐字符串默认左对齐，数字（如整数）默认右对齐，使用<、>或^来强制左、右、中对齐

#convert the value before it is formatted
animal="eels\n"
print(f"My animal is {animal}")
print(f"{animal = }")#animal = 'eels\n',带引号和\n，有点意外。
print(f"My animal is {animal!r}")
print(f"{animal =!r }")#animal = 'eels\n',带引号和\n，不意外。
print(f"My animal is {animal!s}")
print(f"{animal =!s }")#animal =eels<newline>，不带引号，不意外
print(f"My animal is {animal!a}")
print(f"{animal =!a }")#animal ='eels\n'不带引号，不意外，因为都是ascii

#format()
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ''Dcab: {0[Dcab]:d}'
      .format(table))#0=fomat()的第0个参数，不意外0[Sjoerd]访问table中键=Sjoerd的值
#passing the table dictionary as keyword arguments with the ** notation.
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; ''Dcab: {Dcab:d}'
      .format(**table))#同上
#若key值实现未知
# 每轮迭代结果是：{key的名字的字面值}：{key的名字的表达式：整数格式}；
# f只是控制，不会进入字符串
#[]列表推导式，join(),拼接列表字符串,拼接的结果本身是一个带格式控制的字符串
msgFmt=" ".join([f'{k}:'+'{'+k+':d}；' for k in sorted(table.keys())])
print(msgFmt.format(**table))
                 
# table = {k: str(v) for k, v in vars().items()}
# message = " ".join([f'{k}: ' + '{' + k +'};' for k in table.keys()])
# print(message.format(**table))

print(f"{'format()':-^40}")
for x in range(1,11):
    #{0:2d},0=format()第0个参数，2d=宽度为2 的整数，其它类推
    #不要混淆了9.2%，9=总宽度，若超过则不限制，.2%=小数点后保留2位（四舍五入）+%，区别是：之后才是格式规则
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
 
#所以不如f-string简明
print(f"{'f-string':-^40}")#[填充字符][对齐方式][总长度]= [- 填充][居中对齐][总长度40]
for x in range(1,11):
    print(f"{x:2d} {x*x:3d} {x*x*x:4d}")

print(f"{'Manual String Formatting':-^40}")#[填充字符][对齐方式][总长度]= [- 填充][居中对齐][总长度40]
for x in range(1,11):
    #str.rjust()右对齐左填空， 
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))#默认空格分隔，换行结尾

