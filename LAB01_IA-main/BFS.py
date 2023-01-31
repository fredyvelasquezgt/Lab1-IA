from PIL import Image
from ImageReaderBFS import *
from NodeBFS import *
import cv2
import numpy as np

# Basado en: https://github.com/Retrix165/BFS-Image-Maze-Solver

yet_to_see = []
already_seen = []

sur_nodes = ((-1, 0), (0, -1), (0, 1), (1, 0))

# Function to run BFS


def bfs_img(img: Image) -> Image:

    # INTIAL SETUP OF MATRIX AND LISTS
    matrix = imgToMatrix(img)
    start, goal = find_start_end(matrix)
    yet_to_see.append(Coordinate(start[0], start[1], None))
    goal_node = None

    # BFS LOOP

    # While there are nodes left to check
    while yet_to_see:

        # pop first node in 'queue' of yet to see nodes
        cur_node = yet_to_see[0]
        del yet_to_see[0]

        # flag to break search if goal is found
        found = False

        # check surrounding nodes to add to yet to see list
        for r in sur_nodes:
            t_y = cur_node.y + r[0]
            t_x = cur_node.x + r[1]

            # Check if node is valid space and not already seen by program
            if matrix[t_y][t_x] != 'B' and not check_seen_coord(t_y, t_x):
                tmp_node = Coordinate(t_y, t_x, cur_node)
                yet_to_see.append(tmp_node)

                # Remember goal node when found
                if matrix[t_y][t_x] == 'F':
                    goal_node = tmp_node
                    found = True

        # Mark seen node on matrix OPTIONAL
        matrix[cur_node.y][cur_node.x] = 'A'

        if found:
            break

        # add seen node to already seen list
        already_seen.append(cur_node)

    # ENDING GRAPHICS CODE

    # Mark path from goal_node
    if goal_node is not None:
        print("Path found in "+str(goal_node.count)+" steps.")
    else:
        print("Didn't find path to goal node!")

    while goal_node is not None:
        matrix[goal_node.y][goal_node.x] = 'P'
        goal_node = goal_node.parent

    # Mark start and end nodes
    matrix[start[0]][start[1]] = 'S'
    matrix[goal[0]][goal[1]] = 'F'

    outputImg = matrixToImg(matrix)

    return outputImg

# Function to return the positions of the start and end coordinates


def find_start_end(matrix: list) -> list:
    out = [(), ()]
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 'S':
                out[0] = (y, x)
            if matrix[y][x] == 'F':
                out[1] = (y, x)
    if out[0] == () or out[1] == ():
        print("Could not find Start/End")
    return out

# Function to check if coordinate given is already processed or in processing


def check_seen_coord(y: int, x: int) -> bool:
    for i in range(len(already_seen)):
        if already_seen[i].y == y and already_seen[i].x == x:
            return True

    for i in range(len(yet_to_see)):
        if yet_to_see[i].y == y and yet_to_see[i].x == x:
            return True
    return False


def main(filename):
    img = Image.open(filename)
    result_img = bfs_img(img)
    result_img.show()
    ims = np.asarray(result_img)
    cv2.imwrite('ResultadoBFS.png', ims)
