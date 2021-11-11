import AlgorithmsLib.d_star_AtsushiSakai as dstar_A

import AlgorithmsLib.d_star_dynamic_QINQijun as dstar_Q

import AlgorithmsLib.dijkstra as dijkstra

import AlgorithmsLib.a_star as astar

import matplotlib.pyplot as plt

import random

def generate_map(min_x, min_y, max_x, max_y):
    random.seed("ENG1003_w1_Group3 dayo")

    # create boarder
    ox, oy = [], []
        #edge
    for i in range(min_x, max_x + 1): # draw the button border 
        ox.append(i)
        oy.append(min_y)
    for i in range(min_y, max_y + 1): # draw the right border
        ox.append(max_x)
        oy.append(i) 
    for i in range(min_x, max_x + 1): # draw the top border
        ox.append(i)
        oy.append(max_y)
    for i in range(min_y, max_y + 1): # draw the left border
        ox.append(min_x)
        oy.append(i)

    # create start and goal point
    sx = min_x + 1 + int((max_x - min_x - 1) * random.random())
    sy = min_y + 1 + int((max_y - min_y - 1) * random.random())
    while(1):
        gx = min_x + 1 + int((max_x - min_x - 1) * random.random())
        gy = min_y + 1 + int((max_y - min_y - 1) * random.random())
        if((gx - sx) ** 2 + (gy - sy) ** 2 > 70 ** 2):
            break

    #generate block
    density = 0.3 # 0 ~ 1  
    for i in range(min_x + 1, max_x):
        for j in range(min_y + 1, max_y):
            if(random.random() < density and not((i - sx) ** 2 + (j - sy) ** 2 <= 2 or (i - gx) ** 2 + (j - gy) ** 2 <= 2)):
                ox.append(i)
                oy.append(j)
            # if(98 <= (i - sx) ** 2 + (j - sy) ** 2 <= 128):
            #     ox.append(i)
            #     oy.append(j)

    return sx, sy, gx, gy, ox, oy

def two_to_one(list1, list2):
    list_tg = []
    for i in range(0, len(list1)):
        list_tg[i] = [list1[i], list2[i]]
        
    return list_tg

def main():

    min_x = 0
    min_y = 0
    max_x = 70
    max_y = 70

    sx, sy, gx, gy, ox, oy = generate_map(min_x, min_y, max_x, max_y)

    

    # algo_list = {
    #     1 : dstar_A.d_star(max_x - min_x, max_y - min_y, sx, sy, gx, gy, ox, oy),
    #     2 : dstar_Q.d_star(max_x - min_x, max_y - min_y, sx, sy, gx, gy, ox, oy),
    #     3 : "three",
    #     4 : "four"
    # }
    # plt.subplots(1, 3, figsize = (13, 5))

    # plt.subplot(1, 3, 3)
    plt.title("A-star")
    astar.a_star(sx, sy, gx, gy, ox ,oy)
    plt.show()

    # plt.subplot(1, 3, 2)
    plt.title("dijkstra")
    dijkstra.dijkstra(sx, sy, gx, gy, ox ,oy)
    plt.show()
    
    # plt.subplot(1, 3, 1)
    plt.title("Static D-star")
    dstar_A.d_star(max_x - min_x, max_y - min_y, sx, sy, gx, gy, ox, oy)
    plt.show()

    plt.title("Dynamic D-star")
    dstar_Q.d_star(max_x - min_x, max_y - min_y, sx, sy, gx, gy, ox ,oy)
    plt.show()


    
    
    

    # for algo_index in range(1, 3 + 1):
    #     plt.subplot(1, 3, algo_index)
    #     algo_list[algo_index]

    return 0




if __name__ == "__main__":
    main()