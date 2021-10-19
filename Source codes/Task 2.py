import matplotlib.pyplot as plt
import numpy as np
import math

x_min = 0.0 
x_max = 100.0
y_min = 0.0 
y_max = 100.0

C_T = np.arange(x_min, x_max, 0.02)
d_T = 5.0
C_F = 0.00
d_F = 5.0

CLC = [[-1, 0, 0, 0, 0],
       [-1, -1, 0, 0, 0],
       [-1, -1, -1, 0, 0],
       [-1, -1, -1, -1, 0]]
CLC = np.array(CLC)

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

def cal_line(inp, CP):

    CTnCF = d_T * CP[0][0] + d_F * CP[0][1]
    return (CTnCF - d_T * inp) / d_F
    
def SfCP():
    #Search for cross point
    x = 0.0
    CP = []

    for i in range(1,5):    
        if(y_min <= func(0, i) <= y_max):                                            #y-axis
            plt.plot(0, func(0, i), 'o', color = "black")
            CP.append([0, func(0, i)])
    while(x <= x_max and x >= 0.0):
        for i in range(1, 5):
            for j in range(i + 1, 5):
                if(abs(func(x, i) - func(x, j)) <= 0.1 and CLC[i - 1, j - 1] != 1):
                    plt.plot(x, func(x, i), 'o', color = "black")
                    CP.append([x, func(x, i)])
                    CLC[i - 1, j - 1] = 1
            if(abs(func(x, i) - 0.0) <= 0.1 and CLC[i - 1, 4] != 1):                  #x-axis
                    plt.plot(x, 0, 'o', color = "black")
                    CP.append([x, 0])
                    CLC[i - 1, 4] = 1

        x += 0.005
        #if(x >= 39 and x <= 41):
        #    print(func(x, 1) , '\n' , func(x, 2) , '\n' , func(x, 3) , '\n' , func(x, 4) , '\n' , '*')
    
    return CP
            
                


def main():

    plt.xlabel("C_T")
    plt.ylabel("C_F")

    plt.style.use('seaborn-paper')
    plt.grid(True)

    plt.axis([x_min, x_max, y_min, y_max])

    plt.plot(C_T, func(C_T, 1), color = "r", linestyle = "-", linewidth = 1, label = "C_T - C_F <= 30")
    plt.plot(C_T, func(C_T, 2), color = "g", linestyle = "-", linewidth = 1, label = "-0.5C_T - C_F <= -30")
    plt.plot(C_T, func(C_T, 3), color = "b", linestyle = "-", linewidth = 1, label = "2C_T - C_F >= 20")
    plt.plot(C_T, func(C_T, 4), color = "gold", linestyle = "-", linewidth = 1, label = "-4C_T - C_F >= -220")


#    plt.text(75, 38, "C_T - C_F <= 30", color = "r", fontsize = 10)
#    plt.text(1, 43, "-0.5C_T - C_F <= -30", color = "b", fontsize = 10)
#    plt.text(63, 96, "2C_T - C_F >= 20", color = "g", fontsize = 10)
#    plt.text(1, 96, "-4C_T - C_F >= -220", color = "gold", fontsize = 10)

    CP = SfCP() #Search for cross point

#    plt.fill(CP[0], CP[1], CP[2], CP[3], color = "pink", alpha = 0.3)

    #If C_F => ...C_T then use y_max, othervise use y_min

#    plt.fill_between(C_T, func(C_T,1), y_max, color = "r", alpha = 0.5)
 #   plt.fill_between(C_T, func(C_T,2), y_max, color = "b", alpha = 0.5)
  #  plt.fill_between(C_T, func(C_T,3), y_min, color = "g", alpha = 0.5)
   # plt.fill_between(C_T, func(C_T,4), y_min, color = "brown", alpha = 0.5)

    plt.plot(C_T, cal_line(C_T, CP), color = "black", linewidth = 2, label = "Result")

    plt.legend(loc='upper left', bbox_to_anchor=(0.0, 0.95))

    plt.annotate("C_T =" + str(round(CP[0][0], 2)) + "\n" + "C_T =" + str(round(CP[0][1], 2)), xy=(CP[0][0], CP[0][1]), xytext=(4, 60), arrowprops=dict(facecolor='k', headwidth=5, width=1))

    plt.show()

    print("Finished!")

if __name__ == '__main__':
    main()
