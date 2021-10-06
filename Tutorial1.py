def function1():
    print('Charles\nMarcus\nEdmond\nQin Qijun\nWai Ching Cheng')
    

def function2():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    sum = a+b+c
    print(a, b, c, sum)


def function3():
    print('This text represent the content of function 3')  #To be edited by member 3, Replace this line with your actual function code


def function4():
    print('This text represent the content of function 4')  #To be edited by member 4, Replace this line with your actual function code


#The Main function edited by Group leader
print('This is ENG1003'' Week 1 Tutorial Programming Task')
inp = input('Enter the function number to be executed: ')   #Ask for an integer

if inp == '1':
    function1()
elif inp == '2':
    function2()
elif inp == '3':
    function3()
elif inp == '4':
    function4()
else:
    print('There is no function', inp)
