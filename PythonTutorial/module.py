#------------------------------6. Modules-------------------------------
# import defFunc
# fibV=defFunc.fib(100)
#第一次import，会执行 defFunc.py 文件的所有顶层代码
#​模块对象会被缓存到 sys.modules 字典中，键为模块名（defFunc）。
#如何避免导入时运行模块的全部内容？
#​关键方法：将模块中不需要在导入时执行的代码（如测试代码、临时 print()）​放入 if __name__ == "__main__": 块。
#​修改后的 defFunc.py：
# 只有直接运行该文件时才执行以下代码
# if __name__ == "__main__":
#     print("This is a test message")  # 导入时不会执行

from defFunc import fib
fibV=fib(100)

from defFunc import fib as fibo#第二次import，发现sys.modules发现已经存在该模块。​直接使用，不再重新执行。
fibV2=fibo(200)
fibo.__name__

#The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
import sys, defFunc
defFuncNames=dir(defFunc)#必须import defFunc之前的from defFunc import fib 报错defFunc未定义
sysNames=dir(sys)
sysNames