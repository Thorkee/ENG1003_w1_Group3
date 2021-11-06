#################################################################################################
#                                        Instructions
# Developer: QIN Qijun
#




import matplotlib.pyplot as plt

import numpy as np

from sys import maxsize

import math

from numpy.core.fromnumeric import shape

from tkinter import messagebox

show_animation = False

class MAP:

    def __init__(self, x, y, ptype, tag):
        self.x = x
        self.y = y
        self.type = ptype
        self.t = tag
        self.h = maxsize
        self.k = maxsize
        self.b = []
        self.count = 0



class OPENLIST:

    def __init__(self, x_range, y_range):
        self.openlist = ["#"]
        self.hash_value = np.zeros((x_range + 1, y_range + 1), dtype = np.int16)

    def add(self, x, y, value):
        tmp = self.openlist[self.hash_value[x][y]]
        if(tmp != "#" and tmp[2] == value):
            return tmp

        point_data = [x, y, value]

        if(tmp == "#"):
            self.openlist.append(point_data)
            index = len(self.openlist) - 1
            self.hash_value[x][y] = index
        else:
            index = self.hash_value[x][y]
            self.openlist[index] = point_data

        if(index == 1):
            return self.openlist[1][2]
        while(index != 1 and self.openlist[index][2] < self.openlist[math.floor(index/2)][2]):
            tmp = self.openlist[math.floor(index/2)]
            self.openlist[index], self.openlist[math.floor(index/2)] = self.openlist[math.floor(index/2)], self.openlist[index]
            self.hash_value[x][y], self.hash_value[tmp[0]][tmp[1]] = math.floor(index/2), index
            index = math.floor(index/2)

        return self.openlist[1]

    def min_val(self):
        if(len(self.openlist) <= 1):
            return None
        return self.openlist[1]

    def pop(self):
        if(len(self.openlist) <= 1):
            return None

        min_value = self.openlist[1][2]
        length = index = len(self.openlist) - 1

        self.hash_value[self.openlist[1][0]][self.openlist[1][1]] = 0
        self.openlist[index], self.openlist[1] = self.openlist[1], self.openlist[index]
        self.openlist.pop(index)
        length -= 1  

        if(length <= 1):
            return min_value

        min_index = index = 1   
        while(index * 2 <= length):
            if(index * 2 + 1> length):
                min_index = index * 2
            elif(self.openlist[index * 2][2] < self.openlist[index * 2 + 1][2]):
                min_index = index * 2
            else:
                min_index = index * 2 + 1
            tmp1 = self.openlist[index]
            tmp2 = self.openlist[min_index]
            if(tmp2[2] >= tmp1[2]):
                self.hash_value[tmp1[0]][tmp1[1]], self.hash_value[tmp2[0]][tmp2[1]] = index, min_index
                break
            self.openlist[index], self.openlist[min_index] = self.openlist[min_index], self.openlist[index]
            self.hash_value[tmp1[0]][tmp1[1]], self.hash_value[tmp2[0]][tmp2[1]] = min_index, index
            index = min_index

        return min_value




class DSTAR:
    
    def __init__(self, x_range, y_range, ox, oy, start, goal):
        self.ox = ox
        self.oy = oy
        self.obs = self.obstacle(ox, oy)
        self.x_range = x_range
        self.y_range = y_range
        self.start = start
        self.goal = goal
        self.open_list = OPENLIST(x_range, y_range)
        self.map = self.map_init(x_range, y_range)
        self.motion =   [[1, 0],
                        [0, 1],
                        [-1, 0],
                        [0, -1]]

        self.skip = []

    def obstacle(self, ox, oy):
        temp_obs = []
        for i in range(0, len(ox)):
            temp_obs.append([ox[i], oy[i]])
        return temp_obs

    def point_type(self, x, y):
        if([x, y] in self.obs):
            return "#"
        elif(self.start[0] == x and self.start[1] == y):
            return "s"
        elif(self.goal[0] == x and self.goal[1] == y):
            return "g"
        else:
            return "."

    def circle_check(self, x):
        check = x
        while(check.b != [] and check.b.type != "#"):
            self.skip.append(check)
            if(check.b == x or check.b.b == check or check.b in self.skip):
                return True
            check = check.b

        self.skip = []
        return False

    def non_route(self):
        messagebox.showinfo("咫尺相隔两相望","冇有路惹, 過不去惹QAQ\n")
        exit()

    # def neighbor():
        


    def map_init(self, x_range, y_range):
        map_data_row = []
        map_data_line = []
        for i in range(0, y_range + 2):         
            for j in range(0, x_range + 2):                
                map_data_line.append(MAP(i, j, self.point_type(i, j), "new"))
            map_data_row.append(map_data_line)
            map_data_line = []

        self.open_list.add(self.goal[0], self.goal[1], 0)
        map_data_row[self.goal[0]][self.goal[1]].h = 0
        map_data_row[self.goal[0]][self.goal[1]].k = 0

        return map_data_row


    def cost(self, x, y):
        if(x.type == "#" or y.type == "#"):
            return maxsize
        return math.sqrt(math.pow((x.x - y.x), 2) +
                         math.pow((x.y - y.y), 2))


    def process_state(self):
        pos = self.open_list.min_val()
        if(pos == None):
            return -1
        if(pos[2] >= maxsize):
            return -1
        x = self.map[pos[0]][pos[1]]
        k_old = x.k
        self.open_list.pop()
        x.t = self.map[pos[0]][pos[1]].t = "closed"

        if(len(self.skip) > 0):
            if(x in self.skip):
                return
        if(x.count >= 20):
            if(self.circle_check(x)):
                return
            x.count = 0
        x.count += 1

        if show_animation:
            plt.plot(x.x, x.y, "xr", alpha = 0.5)
            plt.pause(0.001)

        if(k_old < x.h):
            for i in enumerate(self.motion):
                if(not(1 <= pos[0] + i[1][0] <= self.x_range and 1 <= pos[1] + i[1][1] <= self.y_range)):
                        continue
                y = self.map[pos[0] + i[1][0]][pos[1] + i[1][1]]

                if((y.h <= k_old and x.h > y.h + self.cost(x, y))
                ):
                # or (y.k < y.h < maxsize and x.h < maxsize and y.h <= k_old + y.h - y.k + self.cost(x, y))
                    if(y.b != x):
                        x.b = y; 
                    x.h = y.h + self.cost(x, y)

        if(k_old == x.h):
            for i in enumerate(self.motion):
                if(not(1 <= pos[0] + i[1][0] <= self.x_range and 1 <= pos[1] + i[1][1] <= self.y_range)):
                    continue
                y = self.map[pos[0] + i[1][0]][pos[1] + i[1][1]]

                if(y.t == "new" or
                (y.b == x and y.h != x.h + self.cost(x, y)) or (y.b != x and y.h > x.h + self.cost(x, y))): 
                    y.b = x 
                    self.insert(y, x.h + self.cost(x, y))
        
        else:
            for i in enumerate(self.motion):
                if(not(1 <= pos[0] + i[1][0] <= self.x_range and 1 <= pos[1] + i[1][1] <= self.y_range)):
                    continue
                y = self.map[pos[0] + i[1][0]][pos[1] + i[1][1]]

                if(y.t == "new" or (y.b == x and y.h != x.h + self.cost(x, y))):
                    y.b = x
                    self.insert(y, x.h + self.cost(x, y))
                elif(y.b != x and y.h > x.h + self.cost(x, y)):
                    y.b = x
                    self.insert(y, x.h + self.cost(x, y))
                elif(y.b != x and x.h > y.h + self.cost(x, y) and y.t == "closed" and y.h > k_old):
                    self.insert(y, y.h)
                    
            

        # else:
        #     for i in enumerate(self.motion):
        #         if(not(1 <= pos[0] + i[1][0] <= self.x_range and 1 <= pos[1] + i[1][1] <= self.y_range)):
        #             continue
        #         y = self.map[pos[0] + i[1][0]][pos[1] + i[1][1]]

        #         if(y.t == "new" or (y.b == x and y.h != x.h + self.cost(x, y))):
        #             y.b = x
        #             self.insert(y, x.h + self.cost(x, y))
        #         else:
        #             if(y.b != x and y.h > x.h + self.cost(x, y)):
                        
        #                 self.insert(x, x.h + self.cost(x, y))
        #             else:
        #                 if y.b != x and x.h > y.h + self.cost(x, y) and y.t == "close" and y.h > k_old:
        #                     self.insert(y, y.h)
		            
				    
				
					
					
						
                
        return x


    def insert(self, x, hnew):
        if(x.t == "new"):
            x.k = hnew
        if(x.t == "open"):
            # if(x.k == hnew or (x.k >=maxsize and hnew >= maxsize)):
            #     return
            # if(x.k < hnew and hnew >= maxsize):
            #     return
            x.k = min(x.k, hnew)
        if(x.t == "closed"):
            # if(x.k == hnew or (x.k >=maxsize and hnew >= maxsize)):
            #     return
            x.k = min(x.k, hnew)
            x.t = "open"
        x.h = hnew
        # if(hnew >= maxsize):
        #     x.h = maxsize
        x.t = "open"
        if show_animation:
            plt.plot(x.x, x.y, "xc", alpha = 0.5)
        
        self.open_list.add(x.x, x.y, x.k)

    def map_updata(self, x):
        self.map[x.x][x.y] = x

    def modify_cost(self, x):
        if x.t == "closed":
            self.insert(x, x.h)
        # if x.t == "circle":
        #     self.insert(x, x.h)
        #     x.t = "new"



    def obstacle_sensor(self, ox, oy, status, current):
        global show_animation
        if(status == "#"):
            amount = min(len(ox), len(oy))

            for i in range(0, amount):
                self.map[ox[i]][oy[i]].type = status
                self.map[ox[i]][oy[i]].h = maxsize
                self.modify_cost(self.map[ox[i]][oy[i]])
                plt.plot(ox[i], oy[i], ".k")
            plt.pause(0.01)

            while(1):
                if(current.b.type != "#"):
                # if(current.count <= 20 and current.b.type != "#"):

                #     if(len(self.skip) > 0):
                #         if(current in self.skip):
                #             return
                #     if(current.count >= 20):
                #         if(self.circle_check(current)):
                #             current.count += 1
                #             current.t = "circle"
                #             # for i in range(0, len(self.skip)):
                #             #     self.skip[i].b = []
                #             continue
                #         current.count = 0
                #     current.count += 1

                    current = current.b
                else:
                    # show_animation = False

                    md_point = current
                    self.modify_cost(md_point)
                    # self.modify_cost(md_point.b)          
                    while(1):
                        feedback = self.process_state()
                        md_point = self.open_list.min_val()

                        if(feedback == -1):
                            break               
                        if(current.b.type == "#"):
                            continue
                        if(md_point[2] >= current.h):
                            break
                        
                    if(feedback == -1):
                        self.non_route()

                    current.b.k = maxsize
                    self.skip = []

                if(current.type == "g"):
                    break

            # md_point = self.map[ox[i]][oy[i]]
            # self.modify_cost(md_point)
            # show_animation = False

            # self.process_state()

            


            # show_animation = True
            # j = int(amount/2)
            # for i in enumerate(self.motion):
            #     if(not(1 <= ox[j] + i[1][0] <= self.x_range and 1 <= oy[j] + i[1][1] <= self.y_range)):
            #             continue

            #     if(self.map[ox[j] + i[1][0]][oy[j] + i[1][1]].b != self.map[ox[j]][oy[j]]):
            #         continue

            #     if(self.map[ox[j] + i[1][0]][oy[j] + i[1][1]].type == "#"):
            #         continue

            #     while(1):
            #         feedback = self.process_state()
            #         md_point = self.open_list.min_val()

            #         if(feedback == -1):
            #             break               
            #         if(md_point[2] >= self.map[ox[j] + i[1][0]][oy[j] + i[1][1]].h):
            #             break

            #     self.map[ox[j]][oy[j]].k = maxsize

            # while(1):
            #         data_cls = self.open_list.min_val()
            #         if(data_cls[2] >= maxsize):
            #             break
            #         self.open_list.pop()


    def run(self):
        global show_animation

        while(1):
            point = self.process_state()          
            if(point == -1):
                exit()
            if(point.type == "s"):
                break
        
        route = point

        # ox = []
        # oy = []
        # for i in range(0, self.x_range):
        #     for j in range(0, self.y_range):
        #         if(i <= 18 or j <= 18):
        #             continue
        #         if(2340 <= (i - self.start[0]) ** 2 + (j - self.start[1]) ** 2 <= 2500):
        #             ox.append(i)
        #             oy.append(j)
        # self.obstacle_sensor(ox, oy, "#")
        
            
        obstacle_generate_1 = False
        obstacle_generate_2 = False
        while(1):

            plt.plot(route.x, route.y, ".r")
            plt.pause(0.001)

#------------------------------------------------------------------------------------------------------------------

            if(route.x <= self.x_range * 0.4 and route.y <= self.y_range * 0.4 and not obstacle_generate_1):
                ox = []
                oy = []
                for i in range(0, self.x_range):
                    for j in range(0, self.y_range):
                        if(not(14 <= i <= 40 and 14 <= j <= 40)):
                            continue
                        if(30 ** 2 <= (i - 45) ** 2 + (j - 45) ** 2 <= 32 ** 2):
                            ox.append(i)
                            oy.append(j)
                self.obstacle_sensor(ox, oy, "#", route)
                obstacle_generate_1 = True

            if(route.x <= 18 and route.y <= 16 and not obstacle_generate_2):
                # show_animation = True
                ox = []
                oy = []
                for i in range(1, 16):
                        ox.append(16)
                        oy.append(i)
                self.obstacle_sensor(ox, oy, "#", route)
                obstacle_generate_2 = True

            # if(route.k == 6):
            #     ox = []
            #     oy = []
            #     for i in range(1, 5):
            #             ox.append(2)
            #             oy.append(i)
            #     self.obstacle_sensor(ox, oy, "#")

            # if(route.k == 4):
            #     ox = [5]
            #     oy = [3]
                
            #     self.obstacle_sensor(ox, oy, "#")
            
            
#------------------------------------------------------------------------------------------------------------------

            if(route.type == "g"):
                break

            if(route.b.type == "#"):
                # show_animation = False

                md_point = route
                self.modify_cost(md_point)
                # self.modify_cost(md_point.b)          
                while(1):
                    feedback = self.process_state()
                    md_point = self.open_list.min_val()

                    if(feedback == -1):
                        break               
                    if(route.b.type == "#"):
                        continue
                    if(md_point[2] >= route.h):
                        break
                    
                if(feedback == -1):
                    self.non_route()

                route.b.k = maxsize
                # while(1):
                #     data_cls = self.open_list.min_val()
                #     if(data_cls[2] >= maxsize):
                #         break
                #     self.open_list.pop()
                # show_animation = False
            
            route = route.b



def d_star(x_range, y_range, sx, sy, gx, gy, ox, oy):

    start = [sx, sy]
    goal = [gx, gy]
    plt.grid(True)
    plt.plot(ox, oy, ".k")
    plt.plot(start[0], start[1], "og")
    plt.plot(goal[0], goal[1], "xb")
    plt.axis("equal")
    plt.pause(0.01)

    d_star = DSTAR(x_range, y_range, ox, oy, start, goal)
    d_star.run()

# def main():

#     x_range = 6
#     y_range = 5
#     ox = [4, 4]
#     oy = [1, 2]
#     for i in range(0, x_range + 2):
#         ox.append(i)
#         oy.append(0)
#     for i in range(0, x_range + 2):
#         ox.append(i)
#         oy.append(y_range + 1)
#     for i in range(0, y_range + 2):
#         ox.append(0)
#         oy.append(i)
#     for i in range(0, y_range + 2):
#         ox.append(x_range + 1)
#         oy.append(i)

#     start = [1, 5]
#     goal = [5, 1]

#     plt.plot(ox, oy, ".k")
#     plt.plot(start[0], start[1], "og")
#     plt.plot(goal[0], goal[1], "xb")
#     plt.pause(0.01)

#     d_star = DSTAR(x_range, y_range, ox, oy, start, goal)
#     d_star.run()



# if __name__ == "__main__":
#     main()

