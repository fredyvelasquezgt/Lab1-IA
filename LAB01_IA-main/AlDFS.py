from PIL import Image
import numpy as np

# Open the maze image and make greyscale, and get its dimensions
from PIL._imaging import display


from DFS import DFS
# Basado en:https://github.com/mralwaleed/maze-solving

import cv2
from Node import Node


def DFSm(filename, s_x, s_y, e_x, e_y):

    image = Image.open(filename).convert('L')
    outimg = image.load()
    binary = image.point(lambda p: p > 128 and 1)
    data = np.array(binary)
    root = None

    x, y = (s_x, s_y)

    gx, gy = (e_x, e_y)

    root = Node(x, y, data)
    list = DFS().Search(root, gx, gy)

    for a in range(len(list)):
        outimg[list[a].y, list[a].x] = 150

    image.show()
    ims = np.asarray(image)
    cv2.imwrite('ResultadoDFS.png', ims)
