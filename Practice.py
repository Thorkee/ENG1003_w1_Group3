def func1():
    print("function 1")

class clss1:
    def __init__(grp, a, b, c, d):
        a = 1
        b = '2'
        c = "hello world"
        grp.d = "hao luan a"
    

def main():

    inp = input("input:")

    if(inp == '1'):
        func1()
    elif(inp == '2'):
        clss1.method1()

if __name__ == '__main__':
    main()
    
        
