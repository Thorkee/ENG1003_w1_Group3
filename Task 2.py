import matplotlib.pyplot as plt
import numpy as np
import math

x_min = 0.0 
x_max = 100.0
y_min = -200.0 
y_max = 180.0

C_T = np.arange(x_min, x_max, 0.02)
d_T = 5.0
C_F = 0.00
d_F = 5.0

def func(inp, sel):
    if(sel == 1):
        return inp - 30.0
    elif(sel == 2):
        return -0.5*inp + 30.0
    elif(sel == 3):
        return 2*inp - 20.0
    elif(sel == 4):
        return -4*inp + 220.0
    else:
        print("The Function is not exist")
        exit()
    
def SfCP():
    #Search for cross point
    x = 0.0
    CP = []
    while(x <= x_max and x >= 0.0):
        for i in range(1, 4):
            for j in range(i + 1, 5):
                if(abs(func(x, i) - func(x, j)) <= 0.02):
                    plt.plot(x, func(x, i), 'o', color = "black")
                    CP.append([x, func(x, i)])
        x += 0.02
        #if(x >= 39 and x <= 41):
        #    print(func(x, 1) , '\n' , func(x, 2) , '\n' , func(x, 3) , '\n' , func(x, 4) , '\n' , '*')
    
    return CP
            
                


def main():

    plt.xlabel("C_T")
    plt.ylabel("C_F")

    plt.style.use('seaborn-paper')
    plt.grid(True)

    plt.axis([0.0, 100.0, -200.0, 180.0])

    plt.plot(C_T, func(C_T, 1), color = "r", linestyle = "-", linewidth = 1)
    plt.plot(C_T, func(C_T, 2), color = "b", linestyle = "-", linewidth = 1)
    plt.plot(C_T, func(C_T, 3), color = "g", linestyle = "-", linewidth = 1)
    plt.plot(C_T, func(C_T, 4), color = "gold", linestyle = "-", linewidth = 1)

    plt.text(75, 25, "C_T - C_F <= 30", color = "r", fontsize = 10)
    plt.text(70, -37, "-0.5C_T - C_F <= -30", color = "b", fontsize = 10)
    plt.text(75, 110, "2C_T - C_F >= 20", color = "g", fontsize = 10)
    plt.text(60, -174, "-4C_T - C_F >= -220", color = "gold", fontsize = 10)

    CP = SfCP()

    plt.show()

if __name__ == '__main__':
    main()