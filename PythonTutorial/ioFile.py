#-----------------7.2. Reading and Writing Files---------------------
from io import SEEK_END, SEEK_SET


file="ioFile.txt"
with open(file, "w",encoding="utf-8") as f:
    f.write("This is the first line.\n")
    f.write("second line.\n")
    f.write("3rd line.\n")

#print(f.closed())#TypeError: 'bool' object is not callable，因为f.closed是个属性，不是方法
print(f.closed)

#------------------------------------7.2.1. Methods of File Objects-------------------------------------------------
# with open(file, "r",encoding="utf-8") as f:
#     print(f"{f.readline()=!r}")#第一行
#     print(f"{f.read()=!r}")#余下全部
#     print(f"{f.read()=!r}")#空
# 类似try-catch，无论正常/异常退出，都会关闭

with open(file, "r+",encoding="utf-8") as f:#"wr"模式错，"w+"模式打开文件时会清空，"r+"模式打开文件时不会清空，但文件不存在会异常
    # print(f"{f.readline()=!r}")#第一行
    # f.seek(0,SEEK_SET)
    # f.write("1st line.\n")#不能覆盖全部，因为覆写行比原行短，结果是：'1st line.\n first line.\n
    # f.seek(0, SEEK_END)
    # f.write("4th line.\n")
    #避免以上bug，读入内存，全部覆写，不过消耗内存
    lines=list(f)
    lines[0]="1st line."
    if len(lines)>=4:
        lines[3]="4th line.\n"
    else:
        lines.append("4th line.\n")

    f.seek(0,SEEK_SET)
    f.writelines(lines)#还是不能完全覆盖，知道“w+”清空的好处了

    f.seek(0,SEEK_SET)
    print(f"{f.read()=!r}")#全部
    print(f"{f.read()=!r}")#空

#binary
with open('workfile', 'rb+') as f:#文件要在运行时目录下，不一定与本.py同一目录,VSCode是工作区目录
    # b'...'存储的是原始字节（0-255的整数）​，用于处理二进制数据。
    # 字符限制：字节字符串中的每个字符必须是ASCII可表示的​（即0-127范围内）。
    # 非ASCII字符（如中文、表情符号）需要转义或通过编码转换生成。
    f.write(b'0123456789abcdef')
    print(f"{f.seek(5)=!r}")    # Go to the 6th byte in the file
    print(f"{f.read(1)=}")      #字节字符串，以b''包裹，显示为b'5'
    print(f"{f.seek(-3, 2)=!r}")    # ​误区1：认为文件末尾是索引15，导致seek(-3,2)定位到索引12。
                                    #​纠正：文件末尾的位置是文件总大小（16），因此seek(-3,2)定位到索引13。
    print(f"{f.read(1)=}")      ##字节字符串，以b''包裹，显示为b'd'

#---------------------------7.2.2. Saving structured data with json-----------------------------------------------
#Encoding basic Python object hierarchies:
import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print(io.getvalue())

#-----------------------------------JSON encoding--------------------
#sep=(item_separator, key_separator)tuple. The default is (', ', ': ')
#To get the most compact JSON representation,you should specify (',', ':') to eliminate whitespace.注意':'中无空格
#compat encoding
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':')))#[1,2,3,{"4":5,"6":7}]最紧凑表示形式，
#Pretty encoding
print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], sort_keys=True, indent=4))#结果见下
# [
#     1,
#     2,
#     3,
#     {
#         "4": 5,
#         "6": 7
#     }
# ]
print(json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=4))#结果见下
# {
#     "4": 5,
#     "6": 7
# }

#customizing JSON object decoding:
import json
def custom_json(obj):
    if isinstance(obj, complex):
        return {'__complex__':True, 'real':obj.real,'imag':obj.imag}
        raise TypeError(f"can't serializ Type {type(obj)}")
encoded=(json.dumps(1+2j,default=custom_json))#default function return a serializable version of obj or raise TypeError.
print(encoded)


#------------------------------------JSON decoding--------------------
decoded=json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
decoded=json.loads('"\\"foo\\bar"')
from io import StringIO
io = StringIO('["streaming API"]')
decoded=json.load(io)

#customizing JSON object decoding:
def as_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"],dct["imag"])
    return dict
decoded=json.loads(encoded,object_hook=as_complex)
print(decoded)

#