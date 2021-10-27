import matplotlib.pyplot as plt

from sys import maxsize

import math

class MAP:

    def __init__(self, x, y, ptype, tag):
        self.x = x
        self.y = y
        self.type = ptype
        self.t = tag
        self.h = maxsize
        self.k = maxsize
        self.b = []


class OPENLIST:

    def __init__(self):
        self.openlist = ["#"]

    def add(self, x, y, value):
        point_data = [x, y, value]
        self.openlist.append(point_data)
        index = len(self.openlist) - 1

        if(index == 1):
            return self.openlist[1][2]
        while(self.openlist[index][2] < self.openlist[math.floor(index/2)][2] and index != 1):
            self.openlist[index], self.openlist[math.floor(index/2)] = self.openlist[math.floor(index/2)], self.openlist[index]
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

        self.openlist[index], self.openlist[1] = self.openlist[1], self.openlist[index]
        self.openlist.pop(index)
        length -= 1  

        if(length <= 1):
            return min_value

        min_index = index = 1   
        while(index * 2 - 1 <= length):
            if(index * 2 > length):
                min_index = index * 2 - 1
            elif(self.openlist[index * 2 - 1][2] < self.openlist[index * 2][2]):
                min_index = index * 2 - 1
            else:
                min_index = index * 2
            self.openlist[index], self.openlist[min_index] = self.openlist[min_index], self.openlist[index]
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
        self.open_list = OPENLIST()
        self.map = self.map_init(x_range, y_range)
        self.motion =   [[1, 0],
                        [0, 1],
                        [-1, 0],
                        [0, -1]]

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
        x = self.map[pos[0]][pos[1]]
        k_old = x.k
        self.open_list.pop()
        x.t = self.map[pos[0]][pos[1]].t = "closed"

        plt.plot(x.x, x.y, "xr", alpha = 0.5)
                # for stopping simulation with the esc key.
        plt.pause(0.001)

        if(k_old < x.h):
            for i in enumerate(self.motion):
                if(not(1 <= pos[0] + i[1][0] <= self.x_range and 1 <= pos[1] + i[1][1] <= self.y_range)):
                        continue
                y = self.map[pos[0] + i[1][0]][pos[1] + i[1][1]]

                if(y.h <= k_old and x.h > y.h + self.cost(x, y)):
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
                    self.insert(x, x.h)
                elif(y.b != x and x.h > y.h + self.cost(x, y) and y.t == "closed" and y.h > k_old):
                    self.insert(y, y.h)
                
        self.map_updata(x)
        self.map_updata(y)
        return self.open_list.min_val()


    def insert(self, x, hnew):
        if(x.t == "new"):
            x.k = hnew
        if(x.t == "open"):
            x.k = min(x.k, hnew)
        if(x.t == "closed"):
            x.k = min(x.k, hnew)
            x.t = "open"
        x.h = x.k
        x.t = "open"
        plt.plot(x.x, x.y, "xc", alpha = 0.5)
        
        self.open_list.add(x.x, x.y, x.k)

    def map_updata(self, x):
        self.map[x.x][x.y] = x

    def modify_cost(self, x):
        if x.t == "close":
            self.insert(x, x.h)


    def obstacle_sensor(self, x, y, status):
        if(status == "#"):
            self.map[x][y].type = status
            self.map[x][y].h = maxsize
            plt.plot(x, y, ".k")


    def run(self):

        while(1):
            kmin = self.process_state()
            point = self.open_list.min_val()
            if(point == None):
                exit()
            if(point[0] == self.start[0] and point[1] == self.start[1]):
                break
        
        route = self.map[point[0]][point[1]]

        self.obstacle_sensor(3, 3, "#")
        self.obstacle_sensor(4, 4, "#")
        while(1):
            if(route.type == "#"):
                self.modify_cost(route)

                while(1):
                    md_point = self.process_state()
                    if(md_point[2] >= self.map[route.x][route.y].h):
                        break

            plt.plot(route.x, route.y, "or")
            plt.pause(0.01)

            if(route.x == self.goal[0] and route.y == self.goal[1]):
                break
            
            route = route.b

        plt.show()


def main():

    x_range = 6
    y_range = 5
    ox = [3, 3]
    oy = [1, 2]
    for i in range(0, x_range + 2):
        ox.append(i)
        oy.append(0)
    for i in range(0, x_range + 2):
        ox.append(i)
        oy.append(y_range + 1)
    for i in range(0, y_range + 2):
        ox.append(0)
        oy.append(i)
    for i in range(0, y_range + 2):
        ox.append(x_range + 1)
        oy.append(i)

    start = [1, 1]
    goal = [5, 1]

    plt.plot(ox, oy, ".k")
    plt.plot(start[0], start[1], "og")
    plt.plot(goal[0], goal[1], "xb")
    plt.pause(0.01)

    d_star = DSTAR(x_range, y_range, ox, oy, start, goal)
    d_star.run()



if __name__ == "__main__":
    main()

