#---------------------------8.3. Handling Exceptions--------------------

while True:
    try:
        
        i=int(input("input a integer:"))
        match i:#Python不用switch，那是C/Java/js的语法
            case 1:
                raise RuntimeError("test")#不必每句加break，不同于C语言
            case 2:
                raise NameError("name error")
            case _:
                print(f"{i=}")
    
        break
    except (RuntimeError,NameError,ValueError) as e:#1.多个异常类型元组，2.as e=异常存为e，以备后用
        print(f"interger !! {e=}")


#根据类的类型捕获，衍生类会被基类捕获，反之不行
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B,C,D,RuntimeError]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
 #    except _:#改正前，错误分析见下
 
    #报错结果理解：        
    ## 第一部分：原始异常（RuntimeError）
    # 发生异常: NameError
    # name '_' is not defined
    #   File "C:\...", line 28, in <module>
    #     raise cls()          # <--- 这里抛出了 RuntimeError
    # RuntimeError:            # 原始异常的根因

    # # 第二部分：处理异常时引发的 NameError
    # During handling of the above exception, another exception occurred:
    #   File "C:\...", line 35, in <module>
    #     except _:            # <--- 处理 RuntimeError 时触发了 NameError
    #            ^
    # NameError: name '_' is not defined
    # ​**During handling of the above exception**：明确说明 NameError 是在处理前一个 RuntimeError 时发生的。
    # ​异常链的传播：Python 会将原始异常（RuntimeError）作为上下文附加到新异常（NameError）中，帮助开发者追踪问题根源。
    #
    # 一、_ 的“通配符”行为是 ​有限场景的语法糖
    # _ 的“通配符”特性 ​仅在特定语法结构​（如 match-case、解包赋值）中生效，​不是全局通用规则。
    # 2. 在解包赋值中忽略值
    # point = (1, 2, 3)
    # x, _, z = point  # 忽略第二个值 

    except Exception as e:#改正后
         print(f"{cls=}")

for cls in [B,C,D,RuntimeError]:
    try:
        inst=cls("arg1","arg2")
        raise inst
    except B:#B/C/D全部被拦截，因为B是C/D的基类
        print(f"B:{inst.args=},{cls.args=}")#B:inst.args=('arg1', 'arg2'),cls.args=<attribute 'args' of 'BaseException' objects>
                                            #实例才会显示args的值，类的类型只会返回args的属性
    except C:
        print("C{cls.args=}")
    except D:
        print(f"D{cls.args=}")
    except Exception as e:
        print(f"{cls=}{e.args=}")

#The most common pattern for handling Exception is to print or log the exception and 
# then re-raise it (allowing a caller to handle the exception as well):
try:
#    filename=input("input filename:")
    with open('workfile','r') as f:#-----8.8. Predefined Clean-up Actions-------------------
        s=f.readlines() #Python的作用域层级:函数（def）、类（class）、模块作用域（全局）
                        #​没有块级作用域​（如if/for/with不会创建新作用域）
                        #但资源有效性需特别注意：with块内的 reader = csv.reader(f)
                        #在with块外，读取其内容，ValueError: I/O operation on closed file
    for l in s:         #所以在with块之外s仍然可用
        print(f"{int(l.strip())=}")
        x=1/0   #导致default Exception被捕获 
except OSError as ose: #open()抛出的FileNotFoundError的父类是OSError
    print(f"{type(ose)}:{ose}")
except ValueError as ve:
    print(ve)
except Exception as e:#-------------------8.10. Enriching Exceptions with Notes-------------------------
    e.add_note("note不会在print()输出")
    e.add_note("但会在重新raise后输出")
    print(f"print不会输出notes {e=}")
    raise   #但会在重新raise后输出
#
else:
    # else 作用：隔离正常流程和异常处理。
    # 举例：如果try块是读取数据，正确读取前提下，else处理，
    # 如果合并在一起，而处理处异常，又被-exept捕获，数据处理的异常会被错误归类为数据读取错误（逻辑混乱）
    #使用else块可以提高代码的可读性，将正常流程和异常处理分开，使得代码结构更清晰。

    #有finally，else还有必要吗？
    #finally用于清理，而else用于处理成功的情况，两者互补而非替代。
    #else块只在没有异常时运行，而finally无论有没有异常都会运行。
    
    print("读取/处理成功")
finally:#-----------------8.7. Defining Clean-up Actions-----------------------
    print("finally clause")

#-------------------8.9. Raising and Handling Multiple Unrelated Exceptions------------------------
