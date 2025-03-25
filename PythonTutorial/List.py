#------------------------------------3.1.2. Text----------------------------------------------
print("C:\some\name")#C:\some<Br>ame
#not to interpret \ as special characters, use raw strings by adding an r before the first quote:
print(r"C:\some\name")##C:\some\name
#Strings can be concatenated (glued together) with the + operator, and repeated with *:
print(3 * 'un' + 'ium')#"unununium"
#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print('Py' 'thon')

#Strings can be indexed (subscripted), with the first character having index 0. 
#没有字符类型，一个字符=长度为1的字符串
word = 'Python'
print(word[0])  #“P"
print(word[5])  #"n"

#Indices may also be negative numbers, to start counting from the right:
print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])  #'P'

#slicing is also supported
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)='Py'
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)='tho'

#indices have defaults; first index default=0, second index default=the size of the string
print(
word[:2],   # character from the beginning to position 2 (excluded)='Py'
word[4:],   # characters from position 4 (included) to the end='thon'
word[-2:]  # characters from the second-last (included) to the end='on'
)

#index out of range
#word[42]#IndexError: string index out of range
#However, out of range slice indexes are handled gracefully when used for slicing:
print(
word[4:42],#'on'
word[42:]#''
)

#strings cannot be changed 
#word[0] = 'J'#TypeError: 'str' object does not support item assignment
#word[2:] = 'py'#TypeError: 'str' object does not support item assignment
#If you need a different string, you should create a new one:
print('J'+word[1:])
print(word[:2]+'py')

print(len(word))

#---------------------------------------------3.1.3. Lists-------------------------------------------------------
#Any changes you make to the list through one variable will be seen through all other variables that refer to it.:
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object
rgba.append("Alph")
print(rgb)#seen through all other variables that refer to it

#shallow copy
correct_rgba = rgba[:]#<-不同于以上rgba = rgb，这里是切片操作，有浅拷贝
print(id(correct_rgba) != id(rgba))  # they reference different object
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

#Assignment to slices is also possible, 
#and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
# replace some values
letters[2:5]=['C', 'D', 'E']
print(letters)

## now remove them
letters[2:5]=[]
print(letters)

# clear the list
letters[:]=[]
print(letters)


#-----------------------------------5.1. More on Lists--------------------------------------------------
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
assert fruits.count("apple")==2, "谁动了我的苹果？"
assert fruits.count("xxx")==0, "xxx哪来的？"
assert fruits.index("banana")==3, "香蕉呢？"
assert fruits.index("banana",4)==6, "另一个香蕉也跑了？"
print(fruits.reverse())#return NONE,can't print
print(fruits)
print(fruits.append("grape"))#return NONE,can't print
print(fruits)
print(fruits.sort())#return NONE,can't print
print(fruits)
print(fruits.pop())#return the last,can print
print(fruits)
print(fruits.copy())#shallow copy：不是“阴影”拷贝，是浅拷贝，深拷贝示例：import copy newlist=copy.deepcopy(fruits)

#----------------------------5.1.1-5.1.2. Using Lists as Stacks & Queues--------------------------------------
#To add an item to the top of the stack, use append(). 
#To retrieve an item from the top of the stack, use pop() without an explicit index.
# 间复杂度是O(1)
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

#
# 
#list as queue
queue=[3,4,5]
queue.append(6)
queue.append(7)
print(queue)
#print(queue.pop(0) if queue.count()>0)
if len(queue)>0:
    print(queue.pop(0))  #slow(because all of the other elements have to be shifted by one).时间复杂度是O(n)

#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. 时间复杂度是O(1)
from collections import deque #Double Ended Queue
queue=deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves
print(queue.popleft())                 # The second to arrive now leaves
print(queue)

#---------------------------------------5.1.3. List Comprehensions-------------------------------------------------
# 即列表推导式，通过 [表达式 for 变量 in 可迭代对象] 的形式，将循环和条件判断压缩到一行代码中，生成新列表。
# 其核心逻辑是：​对可迭代对象中的每个元素应用表达式，并将结果收集到一个新列表中。
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#and it’s equivalent to:
squares=list(map(lambda x:x**2,range(10)))
print(squares)

#and it’s equivalent to:
squares=[x**2 for x in range(10)]#“推导式”名称来源：如数学中定义集合 S={x**2∣x∈N,x<10}
print(squares)

#A list comprehension consists of brackets containing an expression followed by a for clause,
#  then zero or more for or if clauses.
combs=[(x,y)for x in [1,2,3] for y in [3,1,4] if x!=y]
print(combs)

#and it’s equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

#more complex
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print([x*2 for x in vec])

# filter the list to exclude negative numbers
print([x for x in vec if x >= 0])

# apply a function to all the elements
print([abs(x) for x in vec])

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# the tuple must be parenthesized, otherwise an error is raised
#[x, x**2 for x in range(6)]#SyntaxError: did you forget parentheses around the comprehension target?
# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])#​外层循环：遍历 vec 中的每个子列表 elem；
                                            #内层循环:遍历子列表 elem 中的每个元素 num,​将每个 num 收集到新列表中。

#List comprehensions can contain complex expressions and nested functions:
from math import pi
#↓so str(~)="3.0",because round(pi,0)=3.0,not 3,round() return value type = the number type=pi type=float
print([str(round(pi,i)) for i in range(6)]) #['3.0', '3.1', '3.14', '3.142', '3.1416', '3.14159']


#----------------------------------5.1.4. Nested List Comprehensions-------------------------------
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#​推导式的表达式部分包含另一个完整的列表推导式，这里表达式="[row[i] for row in matrix]" =一个嵌套的完整列表推导式
#特征：多层方括号 [[...]]
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

#*,解包matrix之后，将每一行的元素作为单独的可迭代对象传递给zip。
# zip会从每个可迭代对象中依次取出第一个元素，组成第一个元组，然后第二个元素组成第二个元组，依此类推。
print(list(zip(*matrix)))#矩阵转置

#嵌套表达式内外循环交换是否等价？举例如下：
page = ["hello world", "goodbye moon"]
#words=set(word for word in line.split() for line in page)#编译错误：未定义“line”，
#所以把要用的变量尽量定义在外层循环
words=set(word for line in page for word in line.split())
print(words)
#------------------------------5.2. The del statement----------------------------------------------
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)
