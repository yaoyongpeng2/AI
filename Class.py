# 在执行期间的任何时候，都有3到4个嵌套的作用域，其命名空间可以直接访问：

# 最内层作用域（最先被搜索）包含局部名称；
# 任何封闭函数的作用域（从最近的封闭作用域开始搜索），包含非局部但也不全局的名称；
# 倒数第二个作用域包含当前模块的全局名称；
# 最外层作用域（最后被搜索）是包含内置名称的命名空间。

#-------------------------9.2.1. Scopes and Namespaces Example--------------
#global 语句可用于表明特定变量存在于全局作用域中，并且应该在该作用域中被重新绑定；
# nonlocal 语句表明特定变量存在于外层（嵌套）作用域中，并且应该在该作用域中被重新绑定。
def test_scope():
    def do_local():
        spam="local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam="nonlocal spam"
    
    def do_global():
        global spam
        spam="global spam"
    
    spam="test spam"
    do_local()
    print("After do_local():",spam)#test spam
    do_nonlocal()
    print("After do_nonlocal():",spam)#"nonlocal spam"
    do_global()
    print("After do_global():",spam)#"nonlocal spam"


test_scope()#注意缩进，不缩进是全局，缩进就是test_scope()内部，就是无限递归调用，会导致崩溃
            #若在调试时设置断点，无限递归可能导致调试器无法正常暂停（例如断点被频繁触发，最终进程被终止）
print("After test_scope():",spam)#"global spam"


#-----------------9.3. A First Look at Classes---------------------------------------
#-----------------9.3.2. Class Objects-----------------------------------------------
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()
#实例化操作（“调用”一个类对象）会创建一个空对象。
#许多类希望创建的对象的实例被定制为特定的初始状态。因此，一个类可以定义一个名为 __init__() 的特殊方法，如下所示：
def __init__(self):
    self.data = []

#数据属性不需要声明；就像局部变量一样，它们在第一次被赋值时就会自动创建。
#例如，如果x是上面创建的MyClass的一个实例，那么以下代码将输出值16，并且不会留下任何痕迹：
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
#这段代码往类的实例里随意加个属性的能力，破坏了封装性，这种"自由"有什么意义？

#1 灵活性与快速原型开发**
# ​动态扩展对象：允许在运行时为实例添加属性，无需预先在类中定义。这在以下场景非常有用：
# ​临时数据存储：快速测试或调试时临时附加数据。
# ​动态数据处理：解析不确定结构的数据（如 JSON 或数据库记录）时动态绑定字段。

#2 破坏封装性**
# ​不可预测性：随意添加属性可能导致代码难以维护（如属性名拼写错误、意外覆盖）。

# 3. 如何平衡灵活性与封装性？
# ​1) 初始化所有属性（推荐,​初始化属性是约定而非强制,动态添加仍然可以）​
# 在 __init__ 方法中明确初始化所有实例属性，避免运行时随意扩展
#
# class MyClass:
#     def __init__(self):
#         self.counter = 0  # 明确初始化

# 2) 使用 __slots__ 限制属性**
# 通过 __slots__ 声明允许的属性名，禁止动态添加其他属性。
# 
# class MyClass:
#     __slots__ = ["counter"]  # 仅允许 counter 属性
#     def __init__(self):
#         self.counter = 0

# x = MyClass()
# x.counter = 1
# x.other = 2  # ❌ 报错：AttributeError

# 3) 使用 @property 控制访问**（ 封装对特定属性​（如 counter）的读写逻辑，不禁止动态属性）
# 通过属性装饰器封装对属性的访问逻辑。
# 封装对特定属性​（如 counter）的读写逻辑（如类型检查、计算衍生值），而非控制动态属性。
# 
# class MyClass:
#     def __init__(self):
#         self._counter = 0

#     @property
#     def counter(self):
#         return self._counter

#     @counter.setter
#     def counter(self, value):
#         if value < 0:
#             raise ValueError("Counter must be non-negative")
#         self._counter = value

#------------------------9.3.5. Class and Instance Variables------------------
class Dog:
    tricks=[]       # mistaken use of a class variable

    def __init__(self,name):
        self.name=name
        self.tricks=[]  #错误设计没有这一行，类的正确设计应该使用实例变量来代替：
                        #如果在实例和类中都出现了相同的属性名，那么属性查找会优先考虑实例：

    
    def add_trick(self, trick):
        self.tricks.append(trick)
    
a=Dog('A')
b=Dog('B')
print(f"{a.name=},{b.name=}")
a.add_trick('roll over')
b.add_trick('play dead')
print(f"{a.tricks=},{b.tricks=}")   #改正前a.tricks=['roll over', 'play dead'],b.tricks=['roll over', 'play dead']，
                                    #错误：tricks 意外地被所有狗共有
                                    #改正后a.tricks=['roll over'],b.tricks=['play dead']
                                    #如果在实例和类中都出现了相同的属性名，那么属性查找会优先考虑实例：
#-----------------------9.8. Iterators-----------------
#这种访问方式清晰、简洁且方便。迭代器的使用贯穿并统一了 Python
#在幕后，for 语句会调用容器对象的 iter() 方法
#该函数返回一个迭代器对象，迭代器对象定义了 __next__() 方法
#该方法一次访问容器中的一个元素。当没有更多元素时，__next__() 会引发一个 StopIteration 异常
#该异常会通知 for 循环终止。你可以使用内置函数 next() 调用 __next__() 方法

#在了解了迭代器协议背后的机制之后，很容易为你的类添加迭代器行为。
#定义一个 __iter__() 方法，该方法返回一个包含 __next__() 方法的对象。
#如果类中定义了 __next__() 方法，那么 __iter__() 可以直接返回 self
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    
    def __next__(self):
        if self.index==0:
            raise StopIteration()
        self.index -= 1
        return self.data[self.index]

    def __iter__(self):
        return self
    
rev=Reverse('spam')
for char in rev:
    print(char)

#------------------------9.9. Generators--------------------------------
#生成器是一种创建迭代器的简单而强大的工具。
# 它们的编写方式与普通函数类似，但在需要返回数据时使用 yield 语句。
# 每次对其调用 next() 时，生成器会从上次暂停的地方继续执行（它会记住所有的数据值以及最后执行的语句）。

#任何可以用生成器完成的事情，也可以用上一节描述的基于类的迭代器来完成。
# 生成器之所以如此紧凑，是因为 __iter__() 和 __next__() 方法是自动生成的。
# 另一个关键特性是，局部变量和执行状态在调用之间会自动保存。
# 这使得函数比使用实例变量（如 self.index 和 self.data）的方式更易于编写，也更清晰。
# 除了自动生成方法和保存程序状态外，当生成器终止时，它们会自动引发 StopIteration 异常。
# 综合这些特性，生成器可以轻松创建迭代器，而无需比编写普通函数付出更多的努力。
def reverse(data):#->Generator[Any,Any,None]
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse('spam'):
    print(char)


#-------------------9.10. Generator Expressions------------------------------------
#3. 关键区别：生成器 vs 列表推导式
# 特性	       生成器推导式	                                 列表推导式
#=================================================================================
# ​语法	        圆括号 (x for x in iter)	                 方括号 [x for x in iter]
# ​内存占用     低（惰性生成）	                               高（一次性生成所有元素）
# ​适用场景	    大数据流、单次遍历	                           需重复访问或修改的小数据集
# ​函数参数传递	可直接省略外层括号（如 sum(x for x in iter)）   需显式传递列表（如 sum([x for x in iter])）

print(sum(i*i for i in range(10)))#​函数参数传递, 可直接省略外层括号

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec,yvec)))   #直接省略外层括号，点积

#unique_words=set(word for line in page for word in line.split())

data='spam'
print(list(data[index] for index in range(len(data)-1,-1,-1)))#['m', 'a', 'p', 's']
print(data[index] for index in range(len(data)-1,-1,-1))#<generator object <genexpr> at 0x000001677E33BE00>
                                                        #print()不会调用generator的迭代器
