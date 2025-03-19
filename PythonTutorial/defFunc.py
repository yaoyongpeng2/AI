#-------------------------------------4.8Define Functions---------------------------
def fib(n):
    """Print a Fibonacci series less than n."""
    a,b=0,1
    result=[]
    while(a<n):
    #    print(a,end=' ')
        result.append(a)
        a,b=b,a+b
    #print()
    return result
if __name__=="__main__":
    print(fib(100))

#-------------------------------4.9.1 Default Argument-------------------------------------------
def ask_ok(prompt,retries=4,reminder="Please try again!"):
    while True:
        reply=input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries=retries-1
        if retries<0:
            raise ValueError("invalid user response")
        print(reminder)
if __name__=="__main__":
    ask_ok('Do you really want to quit?')
    ask_ok('OK to overwrite the file?', 2)
    ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


#-------------------------------4.9.2 keyword argument------------------------------
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#valid calls
if __name__=="__main__":
    parrot(1000)                                          # 1 positional argument
    parrot(voltage=1000)                                  # 1 keyword argument
    parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
    parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
    parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
    parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


#invalid calls
#parrot()                     #runtime TypeError:parrot() missing 1 required positional argument: 'voltage'
#parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument, SyntaxError: positional argument follows keyword argument
#parrot(110, voltage=220)     # runtime TypeError:parrot() got multiple values for argument 'voltage'
#parrot(actor='John Cleese')  # runtime TypeError:parrot() got an unexpected keyword argument 'actor'


#*name **name parameters
#a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) 
# #containing all keyword arguments except for those corresponding to a formal parameter. 
#a formal parameter of the form *name which receives a tuple 
# containing the positional arguments beyond the formal parameter list. 
# (*name must occur before **name.) Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, 
# meaning that they can only be used as keywords rather than positional arguments.

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)#字符串乘法操作（仅支持字符串与整数相乘）
    for kw in keywords:
        print(kw, ":", keywords[kw])

if __name__=="__main__":
    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#-----------------------------------4.9.3. Special parameters--------------------------------------
#For readability and performance, it makes sense to restrict the way arguments can be passed 
# so that a developer need only look at the function definition to determine 
# if items are passed by position, by position or keyword, or by keyword.
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#      -----------    ----------     ----------
#        |             |                  |
#        |        Positional or keyword   |
#        |                                - Keyword only
#         -- Positional only
#where / and * are optional. 
# If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: 
# positional-only, positional-or-keyword, and keyword-only. 
# Keyword parameters are also referred to as named parameters.
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
if __name__=="__main__":
    standard_arg(2)         #√
    standard_arg(arg=2)     #√

    pos_only_arg(1)         #√
    #pos_only_arg(arg=1)    #runtime TypeError:pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

    #kwd_only_arg(3)         #runtime TypeError:kwd_only_arg() takes 0 positional arguments but 1 was given
    kwd_only_arg(arg=3)

    #combined_example(1, 2, 3)          #runtime TypeError:combined_example() takes 2 positional arguments but 3 were given
    combined_example(1, 2, kwd_only=3)  #√
    combined_example(1, standard=2, kwd_only=3) #√
    #combined_example(pos_only=1, standard=2, kwd_only=3)    #runtime TypeError:combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

#-------------------4.9.4. Arbitrary Argument Lists-----------------------------------
def concat(*args, sep="/"):
    return sep.join(args)
if __name__=="__main__":
    print(concat("earth", "mars", "venus"))
    print(concat("earth", "mars", "venus", sep="."))#*name parameters,can only be followed by keyword parameter.

#--------------------4.9.5. Unpacking Argument Lists-----------------------------------
#The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call 
# requiring separate positional arguments. For instance, the built-in range() function expects separate start and stop arguments. 
# If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:
if __name__=="_main_":
    print(list(range(0,-100,-10)))
    args=[0,-100,-10]
    print(list(range(*args)))#the same result as above

    #In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
    d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    parrot(**d)

    #4.9.6. Lambda Expressions
    # Semantically, they are just syntactic sugar for a normal function definition. 
    pairs=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]
    pairs.sort(key=lambda pair:pair[1])
    print(pairs)#alphabitical order:[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

#4.9.7. Documentation Strings & 4.6. pass Statements
# some conventions:
# 1.The first line short, concise, begin with a capital letter and end with a period.
# 2.If more lines, the second line should be blank
# 3.The first non-blank line after the first line of the string determines the amount of indentation for the entire documentation string.
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

my_function.__doc__

#-----------------4.9.8. Function Annotations--------------------------------------
def f(ham:str, eggs:str="eggs")->str:
    """Demo annotations

    for parameters and return value.
    """
    print("Annotaions:",f.__annotations__)
    print("Arguments:",ham,eggs)
    return f"{ham} and {eggs}"
if __name__=="__main__":
    f("spam")