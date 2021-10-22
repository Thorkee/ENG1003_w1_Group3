"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

This is the simple code for path planning class

"""

egg = 0


import math

import matplotlib.pyplot as plt

import random

import datetime

from tkinter import messagebox

show_animation = True

Delta_F_A = 0.2
Delta_T_A = 0.2

#You can modify the minus-cost area here
C_M_A = -2
d_M_A = 2
M_A_Count = 16
#--------------------------------------    

C_T = 2
d_T = 5
C_F = 1
d_F = 1

class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        """
        Initialize grid map for a star planning


        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution # get resolution of the grid
        self.rr = rr # robot radis
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() # motion model for grid search expansion
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y
#model
        ############you could modify the setup here for different aircraft models (based on the lecture slide) ##########################
        self.C_F = C_F
        self.Delta_F = d_F
        self.C_T = C_T
        self.Delta_T = d_T
        self.C_C = 10
        
#        self.Delta_F_A = 2 # additional fuel
#        self.Delta_T_A = 5 # additional time 
        
        

        self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C

#        print("PolyU-A380 cost part1-> ", self.C_F * (self.Delta_F + self.Delta_F_A) )
#        print("PolyU-A380 cost part2-> ", self.C_T * (self.Delta_T + self.Delta_T_A) )
#        print("PolyU-A380 cost part3-> ", self.C_C )

    class Node: # definition of a sinle node
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        cx, cy = [], []
        while 1:
            if len(open_set) == 0:
                if(show_animation):
                    plt.plot(cx, cy, "xr")
                    plt.pause(0.001)
                global egg
                if(egg == 0):
                    messagebox.showinfo("咫尺相隔两相望","大地江水割南北，彼岸咫尺隔天涯\nThere are no such setbacks that we could not overcome as long as we change the dentisy.\n\nPlease click Ok to modify the dentisy automatically and retry again! :)")
                else:
                    if(egg == 2):
                        emoji = ["If it exists, try again :P", ":)"]
                        egg = -1
                    else:
                        emoji = ["If it exists, that's unfortunate :(", "Xd"]
                    messagebox.showinfo("咫尺相隔两相望","大地江水割南北，彼岸咫尺隔天涯\nThere are no such setbacks that we could not overcome. {0}\n\nPlease click Ok to retry again! {1}".format(emoji[0], emoji[1]))
                return ["egg"], ["egg"], 0

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[o])) # g(n) and h(n): calculate the distance between the goal node and openset
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc", alpha = 0.5)
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                # print("Find goal with cost of -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break
            
            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current
            cx.append(current.x - 10)
            cy.append(current.y - 10)
            # cx.insert(0, current.x)
            # cy.insert(0, current.y)
            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                ## add more cost in time-consuming area
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        # print("time consuming area!!")
                        node.cost = node.cost + Delta_T_A * self.motion[i][2]
                
                # add more cost in fuel-consuming area
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("fuel consuming area!!")
                        node.cost = node.cost + Delta_F_A * self.motion[i][2]
                    # print()
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry, current.cost

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)] # save the goal node as the first point
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    
    def calc_heuristic_maldis(n1, n2):
        w = 1.0  # weight of heuristic
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x) 

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
#        print("min_x:", self.min_x)
#        print("min_y:", self.min_y)
#        print("max_x:", self.max_x)
#        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
#        print("x_width:", self.x_width)
#        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] # allocate memory
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) # grid position calculation (x,y)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy): # Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
                    d = math.hypot(iox - x, ioy - y) # The math. hypot() method finds the Euclidean norm
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True # the griid is is occupied by the obstacle
                        break
#motion
    @staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]

        return motion

def generate_map(min_x, min_y, max_x, max_y, f_width, f_height):
    random.seed(datetime.datetime.now())

    # create fuel consuming area
    fc_x, fc_y = [], []
    f_min_x = min_x + 1 + int((max_x - min_x - f_width - 1) * random.random())
    f_min_y = min_y + 1 + int((max_y - min_y - f_height - 1) * random.random())
    f_max_x = f_min_x + f_width - 1
    f_man_y = f_min_y + f_height - 1
    for i in range(f_min_x, f_max_x + 1):
        for j in range(f_min_y, f_man_y + 1):
            fc_x.append(i)
            fc_y.append(j)

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
        if((gx - sx) ** 2 + (gy - sy) ** 2 > 50 ** 2):
            break

        #random boarder
    density = 0.32 # 0 ~ 1  
    global egg
    if(random.random() < 0.7 and egg == 0):
        if(random.random() < 0.4):
            density = 0.41
        else:
            egg = 2
    else:
        egg == -1
    for i in range(min_x + 1, max_x):
        for j in range(min_y + 1, max_y):
            if(random.random() < density and not((i - sx) ** 2 + (j - sy) ** 2 <= 2 or (i - gx) ** 2 + (j - gy) ** 2 <= 2)):
                ox.append(i)
                oy.append(j)
            if(egg == 2 and 800 <= (i - sx) ** 2 + (j - sy) ** 2 <= 882):
                ox.append(i)
                oy.append(j)

    return fc_x, fc_y, sx, sy, gx, gy, ox, oy

    



#---------------------------------------------------------------------main---------------------------------------------------------------

def main():
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # start and goal position
    grid_size = 1  # [m]
    robot_radius = 0.1  # [m]

    #
    min_x = -10
    min_y = -10
    max_x = 60
    max_y = 60
    f_width = 30
    f_height = 30
    fc_x, fc_y, sx, sy, gx, gy, ox, oy = generate_map(min_x, min_y, max_x, max_y, f_width, f_height)
    
    tc_x, tc_y = [], []
    


    global C_T
    global d_T
    global C_F
    global d_F
    
    global Delta_F_A
    global Delta_T_A
#    global show_animation
    cost = []
    min_cost = 3.4E38
    cost_temp = 0.0
    # show_animation = False
    while(1):
        if True:  # pragma: no cover
            plt.plot(ox, oy, ".k") # plot the obstacle
            plt.plot(sx, sy, "og") # plot the start position 
            plt.plot(gx, gy, "xb") # plot the end position
                
            plt.plot(fc_x, fc_y, "oy", alpha=0.3) # plot the fuel consuming area
            plt.plot(tc_x, tc_y, "or", alpha=0.3) # plot the time consuming area

            plt.grid(True) # plot the grid to the plot panel
            plt.axis("equal") # set the same resolution for x and y axis 

        plt.title("Computing...")
        a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
        rx, ry, cost_temp = a_star.planning(sx, sy, gx, gy)
        if(rx[0] == "egg"):
            global egg
            egg = 1
            rx = ry = []
            plt.cla()
            plt.title("Restarting, please wait...")
            if(show_animation):
                plt.pause(0.001)
            fc_x, fc_y, sx, sy, gx, gy, ox, oy = generate_map(min_x, min_y, max_x, max_y, f_width, f_height)
        else:
            break

    
    plt.title("Finished !")
    plt.plot(rx, ry, "-r", linewidth = 1.5, label = "Minimum Cost Route") # show the route 
    plt.plot(ox, oy, ".k") # plot the obstacle
    plt.plot(gx, gy, "xb") # plot the end position
    plt.plot(0, 0, color = "black", alpha = 0, label = "Total Cost:{0}".format(cost_temp))
    plt.legend(loc='upper left', bbox_to_anchor=(-0.15, 1.15))
    plt.pause(0.001) # pause 0.001 seconds
    plt.show() # show the plot
    
    return 0




if __name__ == '__main__':
    main()

