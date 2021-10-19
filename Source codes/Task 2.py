#################################################################################################
#                                        Instructions
# Developer: ENG1003_20211_A_FPAAE_G3
#
#A. Set an appropriate range for x and y -axis(This step may affect the result)
#B. Set the data of the plane model
#C. Set the amount of lines and the line function(except x and y -axis)
#D. Set the '<', '>' to adjust the line area
#E. Run the program
#*If there is any problem, please contact us at __(Waiting for input)__
#################################################################################################


import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
import math

#A. Set an appropriate range for x and y -axis  
x_min = 0.0 
x_max = 100.0
y_min = 0.0 
y_max = 100.0
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#B. Set the data of the plane model
C_T = np.arange(x_min, x_max, 0.02)
d_T = 5.0
C_F = 0.00
d_F = 5.0
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

CLC = [[-1, 0, 0, 0, 0],
       [-1, -1, 0, 0, 0],
       [-1, -1, -1, 0, 0],
       [-1, -1, -1, -1, 0]]
CLC = np.array(CLC)
CP = []

min_p = []
min_cost = 3.4E38

#C. Set the amount of lines and the line functions(except x and y -axis) in each sel
#You may translate the function into C_F(C_T)=f(C_T) 
#Example: -0.5C_T - C_F <= -30 ----> -0.5*inp + 30.0
Line_Amount = 4                                                 
def line_func(inp, sel):                                       
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
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



#D. Set the '<', '>' and CP to adjust the line area in each sel
#Format:    yi:Point(xi,yi) > or < y=f(xi)
#Example:   For function 3 which you have set (like 2C_T - C_F >= 20)
#           You have to set "CP[p_no][1] > line_func(CP[p_no][0], sel)" in the "if" which means the point isn't in the area
#                               ^                  ^ 
#                  Point(xi,yi)_|                  |_y=f(xi)
def line_area(p_no, sel):                                       #To tell whether the point is in the area or not
    if(CP[p_no][2][0] == sel or CP[p_no][2][1] == sel):
        print(CP[p_no])
        return 0
    if(sel == 1):                                               
        if(CP[p_no][1] < line_func(CP[p_no][0], sel)):   
            CP[p_no][3] = False
    elif(sel == 2):
        if(CP[p_no][1] < line_func(CP[p_no][0], sel)):
            CP[p_no][3] = False
    elif(sel == 3):
        if(CP[p_no][1] > line_func(CP[p_no][0], sel)):
            CP[p_no][3] = False
    elif(sel == 4):
        if(CP[p_no][1] > line_func(CP[p_no][0], sel)):
            CP[p_no][3] = False
    
    return 0
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



    
def SfCP():#Search for cross point
    x = 0.0
    CL = [' ',' ']
    global CP

    for i in range(1,Line_Amount + 1):    
        if(y_min <= line_func(0, i) <= y_max):                                            #y-axis
            plt.plot(0, line_func(0, i), 'o', color = "black")
            CL[0] = i
            CL[1] = 'y'
            CP.append([0, line_func(0, i), CL, True])
            CL = [' ',' ']
    while(x <= x_max and x >= 0.0):
        for i in range(1, Line_Amount + 1):
            for j in range(i + 1, Line_Amount + 1):
                if(abs(line_func(x, i) - line_func(x, j)) <= 0.01 and CLC[i - 1][j - 1] != 1):  #Custom line
                    plt.plot(x, line_func(x, i), 'o', color = "black")
                    CL[0] = i
                    CL[1] = j
                    CP.append([x, min(line_func(x, i), line_func(x, j)), CL, True])
                    CLC[i - 1][j - 1] = 1
                    CL = [' ',' ']
            if(abs(line_func(x, i) - 0.0) <= 0.01 and CLC[i - 1][4] != 1):                  #x-axis
                    plt.plot(x, 0, 'o', color = "black")
                    CL[0] = i
                    CL[1] = 'x'
                    CP.append([x, 0, CL, True])
                    CLC[i - 1][4] = 1
                    CL = [' ',' ']

        x += 0.005
        #if(x >= 39 and x <= 41):
        #    print(func(x, 1) , '\n' , func(x, 2) , '\n' , func(x, 3) , '\n' , func(x, 4) , '\n' , '*')
    
    return 0



def cost(CT, CF):
    return CT * d_T + CF * d_F
def t_line_func(CT):
    return (min_cost - CT * d_T) / d_F

def cal_t_line():
    P_len = len(CP)
    for sel in range(1, Line_Amount + 2):
        for p_no in range(0, P_len):
            line_area(p_no, sel)
    
    global min_cost
    global min_p
    Check = 0
    for p_no in range(0, P_len):
        if(CP[p_no][3] and min_cost > cost(CP[p_no][0], CP[p_no][1])):
            min_cost =  cost(CP[p_no][0], CP[p_no][1])
            min_p = [CP[p_no][0], CP[p_no][1]]
            Check = 1

    if(Check == 0):
        messagebox.showinfo("Error","Minimum point is not exist")
        exit()
    
    return 0



def Init_Matplot():
    plt.xlabel("C_T")
    plt.ylabel("C_F")

    plt.style.use('seaborn-paper')
    plt.grid(True)

    plt.axis([x_min, x_max, y_min, y_max])
    
    #Custom line drawing and the position of the legend
    plt.plot(C_T, line_func(C_T, 1), color = "r", linestyle = "-", linewidth = 1, label = "C_T - C_F <= 30")
    plt.plot(C_T, line_func(C_T, 2), color = "g", linestyle = "-", linewidth = 1, label = "-0.5C_T - C_F <= -30")
    plt.plot(C_T, line_func(C_T, 3), color = "b", linestyle = "-", linewidth = 1, label = "2C_T - C_F >= 20")
    plt.plot(C_T, line_func(C_T, 4), color = "gold", linestyle = "-", linewidth = 1, label = "-4C_T - C_F >= -220")



def Show_Result():#Show the result line with the value and lable
    global min_p

    outp = "Result " + "C_T=" + str(round(min_p[0], 2)) + " C_F=" + str(round(min_p[1], 2))
    plt.plot(C_T, t_line_func(C_T), color = "black", linewidth = 2, label = outp)

    plt.legend(loc='upper left', bbox_to_anchor=(0.0, 0.95))

    plt.annotate("C_T =" + str(round(min_p[0], 2)) + "\n" + "C_T =" + str(round(min_p[1], 2)), xy=(min_p[0], min_p[1]), xytext=(4, 60), arrowprops=dict(facecolor='k', headwidth=5, width=1))

    plt.show()



def main():

    Init_Matplot()

    SfCP() #Search for cross point

    cal_t_line()

    Show_Result()

    print("Finished!")

if __name__ == '__main__':
    main()
