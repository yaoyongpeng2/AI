#--------------------5.3. Tuples and Sequences-----------------------------------------------------
t=12345,54321,"hello"
print(t[0])
#Nested tuple
u=t,(1,2,3,4,5)
print(u)

#tuple is immutable
#Though tuples may seem similar to lists, they are often used in different situations and for different purposes. 
# usually tuples-> 不同类型的 elements; Lists-> homog同类型的 elements.
#t[0]=888 #TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[0][0]=10
print(v)

#tuples containing 0 or 1 items
empty=()
singleton="hello",# <-- note trailing comma,Ugly, but effective. 
singleton2=("hello")
print(len(empty))
print(singleton)
print(singleton2)

#tuple packing and unpacking
t=12345,54321,"hello"#packing
x,y,z=t#unpacking
print(f"x={x}|y={y}|z={z}")

#-----------5.4. Sets--------------------------------------------------------------------
#created by {}
basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)# show that duplicates have been removed
print("orange" in basket)#True
print("crabgrass" in basket)#False

#Set opertions
a = set('abracadabra')
#对比：以上basket的构建，元素必须用逗号分隔，每个元素被视为一个整体。
#这里set() 的参数必须是一个可迭代对象​，如果传入字符串，会将其视为由字符组成的可迭代对象，逐个拆分为独立元素。
# 如果a = set(['abracadabra'])  # 结果：{'abracadabra'}
b = set('alacazam')
#可在VSCode调试控制台查看变量值，不必print()
a                                  # unique letters in a
b                                  # unique letters in b
a - b                              # letters in a but not in b
a | b                              # letters in a or b or both
a & b                              # letters in both a and b
a ^ b                              # letters in a or b but not both

#Similarly to list comprehensions, set comprehensions are also supported:
#不同之处：列表推导式用[]，如lista=[x in 'abracadabra' if x not in'abc' ]
#a={x in 'abracadabra' if x not in'abc' }#语法错误：格式 {表达式 for 变量 in 可迭代对象}
a={x for x in 'abracadabra' if x not in'abc' }
a#{'r', 'd'}
lista=[x for x in 'abracadabra' if x not in'abc' ]
lista#['r', 'd', 'r']，比Set多一个'r'，因为list不去重

#----------------5.5. Dictionaries------------------------------------------------------------------------------
#a dictionary as a set of key: value pairs,  A pair of braces creates an empty dictionary: {}. 
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; 
# this is also the way dictionaries are written on output.

#The main operations on a dictionary are storing a value with some key and extracting the value given the key. 
# It is also possible to delete a key:value pair with del. 
# If you store, using a key that is already in use, the old value associated with that key is forgotten. 因为键须唯一
# It is an error to extract a value using a non-existent key.
# To check whether a single key is in the dictionary, use the in keyword.

tel={"jack":4001,"rose":4002,"captin":4003}#创建
tel["titanic"]=4000#增加
tel["titanic"]=4010#修改也是覆盖
del tel['titanic']#删除
tel['jack']
"titanic" in tel#False
"jack" not in tel#False
list(tel)#in insertion order
sorted(tel)#in alphabetical order

#created directly from sequences of key-value pairs:
#tel=dict([("jack":4001),("rose":4002),("captin":4003)])

# 关于 dict() 构造函数的参数规则与 tuple 关键字的完整解释：
# ---------------------------------------------------------------------
# 1. dict() 的构造函数接受一个可迭代对象（Iterable），其每个元素必须是一个包含两个元素的元组 (key, value)
#    - 正确示例：dict([("key1", 1), ("key2", 2)])
#    - 错误示例：dict([("key1": 1), ("key2": 2)])  # 元组内不能用 : 分隔

# 2. 语法核心规则：
#    - 在字典字面量 {} 中，键值对用 : 分隔（如 {"key": value}）
#    - 在元组中，元素用 , 分隔（如 (key, value)）
#    - dict() 的参数是元组列表，因此必须用 , 分隔键值

# 3. tuple 关键字的说明：
#    - tuple 是 Python 的内置关键字，用于定义元组类型
#    - 在类型注解中，tuple[...] 是合法的泛型语法，用于声明元组元素类型
#      * 示例：tuple[str, int] 表示一个包含字符串和整数的元组
#      * 注意：在普通代码中直接写 tuple[str, int] 会报错（需 Python 3.9+ 或 from __future__ import annotations）

# 4. 类型注解 Iterable[tuple[_KT, _VT]] 的解释：
#    - Iterable 表示可迭代对象（如列表、生成器）
#    - tuple[_KT, _VT] 表示每个元素是包含两个元素的元组：
#      * _KT（Key Type）：键类型（如 str/int 等）
#      * _VT（Value Type）：值类型（任意类型）
# ---------------------------------------------------------------------
tel=dict([("jack",4001),("rose",4002),("captin",4003)])

#created from dict comprehensions
squares={x:x**2 for x in range(10)}#对比Set=都用{}，不同指出键值对 vs 单有值
squares


#----------------5.6. Looping Techniques------------------------------------------------------------------
#looping through dictionaries
knights={'gallahad': 'the pure', 'robin': 'the brave'}
#{print(key,val) for key,val in knights}#ValueError: too many values to unpack，因为字典默认遍历的是键,而不是键值对。
{print(key,val) for key,val in knights.items()} #正确，因为items()返回键值对，
                                                #使用花括号的推导式可以是字典推导式或集合推导式，具体取决于是否包含键值对。
                                                # print()返回NONE，所以这是个集合推导式，返回很多，去重后只有一个None

#index and corresponding value can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):#enumerate()产生一个位置索引+值对，如 (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    print(i,v)

#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions=['name', 'quest', 'favorite color']
answers=['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions, answers):
    print(f"What's your {q}, It's {a}")
#    print("What's your {0}, It's {1}".format(q,a))#同上