import sys
from collections import deque
from turtle import st

class Node:
    def __init__(self, pos, cost):
        self.pos = pos
        self.cost = cost

def create_node(x, y, c):
    val = grid_pos(x, y)
    return Node(val, c + 1)

class grid_pos:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def generate_maze(file):
    f = open(file, "r")
    s = f.read()
    f.close()
    lines = s.split('\n')
    # get a list of lists with each character as a separate element

    maze = []

    for line in lines:
        temp = []
        for character in line:
            temp.append(character)
        if(len(temp) > 0):
            maze.append(temp)
    
    return maze

def get_starting_position(maze):
    starting_pos = grid_pos(0,0)


    for lineNumber, line in enumerate(maze):
        for charNumber, char in enumerate(line):
            if(line[charNumber] == 'S'):
                starting_pos = grid_pos(lineNumber, charNumber)

    return starting_pos

def get_ending_position(maze):
    ending_pos = (0, 0)


    for lineNumber, line in enumerate(maze):
        for charNumber, char in enumerate(line):
            if(line[charNumber] == 'G'):
                ending_pos = grid_pos(lineNumber, charNumber)

    return ending_pos

def dfs(Grid, dest: grid_pos, start: grid_pos):
    adj_cell_x = [1, 0, 0, -1]
    adj_cell_y = [0, 1, -1, 0]
    m, n = (len(Grid[0]), len(Grid))

    visited_blocks = [[False for i in range(m)]
               for j in range(n)]


    visited_blocks[start.x][start.y] = True
    stack = deque()
    sol = Node(start, 0)
    stack.append(sol)
    neigh = 4
    neighbours = []
    cost = 0



    while stack:
        current_block = stack.pop()
        current_pos = current_block.pos
        x_pos = current_pos.x
        y_pos = current_pos.y
     
        for i in range(neigh):

            # print(str(x_pos) + " " + str(y_pos))
            # print(str(dest.x) + " " + str(dest.y))
            if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                x_pos = current_pos.x
                y_pos = current_pos.y + adj_cell_y[i]
            if y_pos == 0 and adj_cell_y[i] == -1:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y
            else:
                x_pos = current_pos.x + adj_cell_x[i]
                y_pos = current_pos.y + adj_cell_y[i]
            if x_pos < n and x_pos != -1 and y_pos < m and y_pos != -1:

                if x_pos == dest.x and y_pos == dest.y:
                    print("Total nodes visited = ", cost)
                    return current_block.cost

                if Grid[x_pos][y_pos] == '%':
                    if not visited_blocks[x_pos][y_pos]:
                        cost += 1
                        visited_blocks[x_pos][y_pos] = True
                        stack.append(create_node(x_pos, y_pos, current_block.cost))
    return -1

maze = generate_maze("maze3.txt")

starting_pos = get_starting_position(maze)
ending_pos = get_ending_position(maze)

result = dfs(maze, ending_pos, starting_pos)

print(result)


