def function1():
    print('Charles\nMarcus\nEdmond\nQuintinUmi\nMinnie')
    

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
    print("pls replace this line with your code")
    

def extrafunction6():
    F_n, S_n = 0,0
    F_n = input("First number: ")
    S_n = input("Second number: ")
    print("The sum is " + str(int(F_n) + int(S_n)))


def extrafunction7():
    n=input("List length:")
    n=int(n)
    while n>0:
        print(n)
        n-=1


def extrafunction8():
    side = int(input("Square Size : "))
    print("Square Number Pattern") 
    for i in range(side):
        for i in range(side):
            print('[ ]', end = ' ')
        print()

def eventualfunction():
    import random
    a = random.randint(50,200)
    num = random.randint(1, a)
    guess = None
    attempt = 0
    print("The range for this round is 1 -", a)

    while guess != num:
        guess = input('Make a guess:')     
        guess = int(guess)
        attempt+=1
        if guess < num:
            print("The range is now", guess, "-", a)
            continue
        elif guess > a:
            print("You can not make any guessing exceeding", a)
            continue
        elif guess > num and guess < a+1:
            print("The range is now", 1, "-", guess)
        else:
            if attempt == 1:
                print("BINGO! You took 1 attempt to reach the answer!" )
            else:
                print("BINGO! You took", attempt, "attempts to reach the answer!" )
            break
            


print("This is ENG1003'' Week 1 Tutorial Programming Task")

inp1 = input('Would you like to try the extra code(Y/N): ')

if ord(inp1) > 90 and len(inp1) == 1:
    inp1 = chr(ord(inp1) ^ 0x20)

if inp1 == "N":
    inp = input('Enter the function number (from 1 to 4) to be executed: ')
    if inp == '1':
        function1()
    elif inp == '2':
        function2()
    elif inp == '3':
        function3()
    elif inp == '4':
        function4()
    else:
        print("There is no function", inp)

elif inp1 == "Y":
    inp2 = input('Enter the function number (from 1 to 5, 5 means the number guessing game) to be executed: ')
    if inp2 == '1':
        extrafunction5()
    elif inp2 == '2':
        extrafunction6()
    elif inp2 == '3':
        extrafunction7()
    elif inp2 == '4':
        extrafunction8()
    elif inp2 == '5':
        eventualfunction()
    else:
        print('There is no function', inp2)
else:
    print("You can only answer Y for yes or N for no, thank you")