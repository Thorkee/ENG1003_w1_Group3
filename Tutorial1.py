def function1():
    print('Charles\nMarcus\nEdmond\nQin Qijun\nWai Ching Cheng')
    

def function2():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    sum = a+b+c
    print("The sum of", a,",", b, "and", c, "is", sum)


def function3():
    a = int(input("Enter the number that will be squared:"))
    b = a**2
    print("The square of", a, "is", b)


def function4():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    if a>b:
        print("a is larger than b.")
    elif a==b:
        print("a is equal to b")
    elif a<b:
        print("b is larger than a")
    else:
        print("Sorry my brother, I'm not that advanced to solve your input numbers. Have a nice day anyway!")

def extrafunction5():
    

def extrafunction6():


def extrafunction7():


def extrafunction8():


print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number (from 1 to 4) to be executed: ')

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
elif inp == '5':
    extrafunction5()
elif inp == '6':
    extrafunction6()
elif inp == '7':
    extrafunction7()
elif inp == '8':
    extrafunction8()
else:
    print('There is no function', inp)