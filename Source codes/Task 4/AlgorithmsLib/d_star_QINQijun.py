from _typeshed import Self
import matplotlib as plt

from sys import maxsize

import math

class MAP:

    def __init__(self, x, y, ptype):
        self.x = x
        self.y = y
        self.type = ptype
        self.t = ""
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

        min_index = index = 1   
        while(index * 2 - 1 <= length):
            if(index * 2 > length):
                min_index = index * 2 - 1
            elif(self.openlist[index * 2 - 1][2] < self.openlist[index * 2][2]):
                min_index = index * 2 - 1
            else:
                min_index = index * 2
        self.openlist[index], self.openlist[min_index] = self.openlist[min_index], self.openlist[index]

        return min_value




class DSTAR:
    
    def __init__(self, x_range, y_range, ox, oy, start, goal):
        self.ox = ox
        self.oy = oy
        self.start = start
        self.goal = goal
        self.open_list = OPENLIST()
        self.map = self.map_init(x_range, y_range)
        self.motion =   [[1, 0],
                        [0, 1],
                        [-1, 0],
                        [0, -1]]

    def point_type(self, x, y):
        if(self.ox == x and self.oy == y):
            return "#"
        elif(self.start[0] == x and self.start[1] == y):
            return "s"
        elif(self.goal[0] == x and self.goal[1] == y):
            return "g"
        else:
            return "."


    def map_init(self, x_range, y_range):
        map_data_row = []
        map_data_line = []
        for i in range(0, y_range + 2):
            for j in range(0, x_range + 2):
                map_data_line.append(MAP(i, j, self.point_type(i, j)))
            map_data_row.append(map_data_row)
            map_data_line.clear()

        self.open_list.add(self.goal)
        map_data_line[self.goal[0]][self.goal[1]].t = "new"
        map_data_line[self.goal[0]][self.goal[1]].h = 0
        map_data_line[self.goal[0]][self.goal[1]].k = 0

        return map_data_row

    def cost(x1, y1, x2, y2):
        return math.sqrt(math.pow((x1 - x2), 2) +
                         math.pow((y1 - y2), 2))

    def map_edit(self, x, y, status):
        self.map[x][y].type = status

    def process_state(self):
        pos = self.open_list.min_val()
        if(pos == None):
            return -1
        x = self.map[pos[0]][pos[1]]
        k_old = self.open_list[pos[0]][pos[1]]
        self.open_list.pop()


        for i in enumerate(self.motion):
            y = self.map[pos[0] + i[0]][pos[1] + i[1]]


    def min_state():
        pass

    def insert():
        pass

    def modify_cost():
        pass


