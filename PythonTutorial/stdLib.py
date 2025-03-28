#----------------10.1. Operating System Interface-------------------
import os
cwd=os.getcwd()
print(cwd)
os.chdir("../")
print(os.getcwd())
os.system('mkdir test-os')
os.rename('test-os','test-os2')
print(os.listdir())
os.rmdir('test-os2')
#print(dir(os))
#print(help(os))

import shutil
os.chdir(cwd+'/../')
#os.mkdir('./build/executables')#仅单层目录
os.makedirs('./build/executables',exist_ok=True)#可多层，已存在，可覆盖
shutil.copy('workfile','./build/executables/workfile.txt')
#防止下一行报错：目标路径“installdir\executables”已存在
#os.removedirs('installdir')#能删除非空子目录
shutil.rmtree('installdir')#能删除目录树，无论子目录是否非空
print(shutil.move('./build/executables','installdir'))#见以下注释
# 总结：关键逻辑表
# =========================================================================================
# 目标状态                    | shutil.move 行为                     | 解决方法
# -----------------------------------------------------------------------------------------
# 目标不存在且父目录存在       | 重命名源为 installdir                | 直接调用 shutil.move
# 目标不存在且父目录不存在     | 报错 FileNotFoundError               | 先创建父目录 os.makedirs
# 目标存在且是目录             | 移动源到目标目录内                   | 直接调用 shutil.move
# 目标存在且是文件             | 报错 NotADirectoryError              | 删除文件或修改目标路径
# 目标存在且需覆盖             | 报错 shutil.Error                    | 先删除旧目录 shutil.rmtree
# =========================================================================================

#-----------------------------------10.2. File Wildcards----------------------
os.chdir(cwd)
import glob
print(glob.glob('*.py'))
#-----------------------------10.3. Command Line Arguments--------------------
import sys
print(sys.argv)

import argparse
parse=argparse.ArgumentParser(description='Show top lines from each file')
#.vscode/launch.json，增加了"args": ["Class.py ", "${file}", "-l", "5"]
parse.add_argument('filenames',nargs='+')#filenames位置参数（无前缀-），'+'=至少一个
parse.add_argument('-l','--lines',type=int,default=10)#-l/--lines可选参数（前缀-），行数（默认 10，须为整数）
args=parse.parse_args() #按照add_argument()给的参数结构，
                        #解析命令行参数（=sys.argv=lanch.json文件的args项的值）
print(args)

#--------------0.4. Error Output Redirection and Program Termination---------
sys.stdout.write("Warning to stderr\n")

#------------------10.5. String Pattern Matching--------------------------------
import re
print(re.findall(r"\bf[a-z]*","which foot or hand fell fastest"))#\b表示单词的边界（=词头或词尾）
print(re.sub(r"(\b[a-z]+) \1",r"\1","cat in the the hat"))  #两个相同且相邻的词，此处两个the，去掉一个
                                                            #r"\1"前的r不能少，否则"\1"为空
print(re.sub(r"(\b[a-z]+) \1",r"\1","cat in the the the hat"))  #若三个相同且相邻的词，前两个去一个，第三个不去
                                                                #因为读第三个时，之前的已经处理完，不会往回看
#当只需要简单的功能时，优先使用字符串方法，因为它们更易于阅读和调试。
print("tea for too".replace("too","two"))

#-------------------10.6. Mathematics-----------
import math
print(math.cos(math.pi/4))
print(math.log(1024,2))#结果=10.0,2**x=1024, 其中x=log(1024,2)，不要搞反了。

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(['apple', 'pear', 'banana'],1))
print(random.sample(range(100),10))
print(random.random())
print(random.randrange(6))

import statistics
data=[2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

#-----------------------------10.7. Internet Access---------------------
from urllib.request import urlopen
from urllib.error import URLError
import socket
try:
    with urlopen("http://worldtimeapi.org/api/timezone/etc/UTC.txt",timeout=10) as resp:
        content=resp.read().decode()
        for line in content.splitlines():
    #        line= line.decode()
            if line.startswith("datetime:"):
                print(line.rstrip())
except URLError as e:
    print(f"URL 错误: {e.reason}")
except socket.timeout:
    print("请求超时")
except ConnectionResetError as e:
    print(f"连接被重置: {e}")
except Exception as e:
    print(f"{e}")

import smtplib
# server=smtplib.SMTP('localhost')
# server.sendmail('yaoyongpeng@qq.com','yaoyongpeng@qq.com',
# """To:yaoyongpeng@qq.com
#     From:yaoyongpeng@qq.com
#     Python stdlib-smtplib test.
# """)
# server.quit()
from email.mime.text import MIMEText
sender='yaoyongpeng@qq.com'
reciever=sender
content="Python发送的邮件"
subject="Python发送邮件测试"
mail=MIMEText(content,'plain','utf-8')
mail['from']=sender
mail['to']=reciever
mail['subject']=subject
try:
    with open('../auth-code.txt')as f:
        password=f.read()
        password=password.strip()
    server=smtplib.SMTP_SSL("smtp.qq.com",465)#SSL加密
    #授权码获得步骤，进入网页版QQ邮箱：
    # 【设置】→【账号与安全】→【安全设置】→【POP3/IMAP/SMTP/Exchange/CardDAV 服务】
    #→【开启服务】，经过验证，会产生授权码，可用于第三方收发邮件
    server.login(sender,password)
    server.sendmail(sender,reciever,mail.as_string())
except FileNotFoundError as e:
    print(f"授权码文件找不到{e}")
except Exception as e:
    print(f"发送失败{e}")
finally:
    server.quit()

#---------------10.8. Dates and Times------------
from datetime import date
now=date.today()
print(now)
birth=date(1973,11,17)

# age=now-birthday
# print(age.strftime())
year=now.year-birth.year
if(now.month,now.day)<(birth.month,birth.day):
    year-=1
    print(f"{year=},{(now-birth).days=}")
# month=now.month-birth.month
# day=now.day-birth.day
# age=date(year,month,day)
# if day<0:
#     month -=1

#----------------------------10.9. Data Compression--------------------
import zlib
s=b'witch which has which witches wrist watch'#b=以字节（不是字符）存储
t=zlib.compress(s)
print(f"{len(s)=},{len(t)=}")
dec=zlib.decompress(t)
print(f"{len(dec)=}")
print(f"{zlib.crc32(dec)=}")#计算数据的CRC - 32校验和
                            #(Cyclic Redundancy Check）32位版本。它是一种数据传输检错功能。)。

#--------10.10. Performance Measurement-------------------------
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())#0.03079770000113058
print(Timer('a,b = b,a', 'a=1; b=2').timeit())#0.021722699999372708
#一个要计时的语句+一个用于设置的附加语
#使用元组打包和解包特性比传统的参数交换方法更快，Python 解释器对元组操作有优化，效率更高。
#反编译字节码观察底层差异：
# t=a; a=b; b=t，共6步
#   2           0 LOAD_NAME                0 (a)
#               2 STORE_NAME               1 (t)

#   3           4 LOAD_NAME                2 (b)
#               6 STORE_NAME               0 (a)

#   4           8 LOAD_NAME                1 (t)
#              10 STORE_NAME               2 (b)
#              12 LOAD_CONST               0 (None)
#              14 RETURN_VALUE
#-------------------------------------------------------------
# a,b = b,a 共5步
#  1           0 LOAD_NAME                0 (b)
#               2 LOAD_NAME                1 (a)
#               4 ROT_TWO
#               6 STORE_NAME               1 (a)
#               8 STORE_NAME               0 (b)
#              10 LOAD_CONST               0 (None)
#              12 RETURN_VALUE

#-----------------------10.11. Quality Control-------------------------
#doctest 模块提供了一种工具，用于扫描模块并验证嵌入在程序文档字符串中的测试。
# 测试的构建非常简单，只需将典型的函数调用及其结果剪切并粘贴到文档字符串中即可。
# 这不仅通过为用户提供示例来改进文档，还允许 doctest 模块确保代码与文档保持一致。

def average(values):
    """AI is creating summary for average

    Args:
        values ([type]): [description]
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)

import doctest
doctest.testmod()#标识是'>>> '（有个空格）

#unittest 模块不像 doctest 模块那样毫不费力，
# 但它允许在单独的文件中维护更全面的测试集。
import unittest

class TestStatisticalFunctions(unittest.TestCase):#类名Test开头

    def test_average(self):#方法名test_开头
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])#len(values)==0
        with self.assertRaises(TypeError):
            average(20, 30, 70)#需要列表类型

#unittest 支持多种命令行参数来控制测试行为，例如：
# ​指定测试用例：python test.py TestClass.test_method
# ​输出详细结果：python test.py -v
# ​过滤测试：python test.py -k "pattern"
# ​并行测试：python test.py --workers=2
# sys.argv[0:]=[]#是因为本脚本的输入参数，
               #unittest.main（）不认识，故报错，清除多余，则不报错了
                #argv[0]保留，否则下一句IndexError: list index out of range
# unittest.main()
unittest.main(argv=[""])#比修改sys.argv更好
