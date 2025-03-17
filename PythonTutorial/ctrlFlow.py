#-4.1 if statements---
# ":",if-elif-else,int(),input()的使用
x=int(input("Input an Tnteger:"))
if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')

#-4.2 for statements---
words=['cat', 'window', 'defenestrate']
for w in words:
    print(w,len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}  #Tuples

# Strategy1:  Iterate over a copy
for user,status in users.copy().items():
    if status=='inactive':
        del users[user]
    
# Strategy2:  Create a new collection
active_users={}
for user,status in users.items():
    if status=='active':
        active_users[user]=status

#-4.3 range()--
for i in range(5):
    print(i)

for i in range(5,10):#5,6,7,8,9
    print(i)

print(range(5,5))#输出结果就是“range(5,5)”
for i in range(5,5):#起止相同会如何？空，啥也不干。
    print(i)

for i in range(0,10,3):
    print(i)

for i in range(-10,-100,-30):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i], end=',\n')

print("sum(range()):",sum(range(5)))

#-4.4 break and continue and 4.5 else clause---
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(f"{n} equals {x} * {n//x}")#f"..."：格式化字符串字面值，嵌入的变量或表达式用 {} 包裹。
                                             #n//x,n/x 的整数商（向下取整）,如6//2=3, 但6/2=3.0
            break#是否合数，有一个即可，这个内循环可以break，不必继续
    else:# If the loop finishes without executing the break, the else clause executes.
        print(f"{n} is a prime number")

for n in range(2,10):
    if n%2==0:
        print(f"found an even number {n}")#若无f...,则输出“found an even number {n}”
        continue#循环本轮后面义务必要，直接下一轮
    print(f"found an odd number {n}")

#pass statement is ignored

#match statement to be added,after Class.
