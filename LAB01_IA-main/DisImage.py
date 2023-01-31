from PIL import Image
from matplotlib import pyplot
import numpy as np
from matplotlib import image
import matplotlib.pyplot as plt
import scipy.misc
import matplotlib
import cv2

terreno = (255, 255, 255, 255)
pared = (0, 0, 0, 255)
inicio = (255, 0, 0, 255)
meta = (0, 255, 0, 255)
# Indicamos el color del camino resultado


# Creamos la funcion que nos permitira discretizar la imagen , cabe mencionar que la imagen debe de estar en formato BMP


def RenderImage(filename):

    image = filename

    # pyplot.imshow(p)
    # pyplot.show()

    # Definimos la matrix
    matrix = []
    m = []
    # Inicializamos el punto de inicio del laberinto
    s_x, s_y = 0, 0
    # Inicializamos el punto final del laberinto
    e_x, e_y = 0, 0
    # Abrimos la imagen
    im = Image.open(image)
    im = im.resize((280, 280))

    width, height = im.size

    r_total = 0
    g_total = 0
    b_total = 0
    count = 0
    c_pixel = 0

    newImage = []

    print(height, width)

    for i in range(0, width):

        newImage.append([])
        for j in range(0, height):
            r_total = 0
            g_total = 0
            b_total = 0
            count = 0
            r_t = 0
            g_t = 0
            b_t = 0

            pixel = im.getpixel((j, i))

            for y in range(5):
                r_total = 0
                g_total = 0
                b_total = 0
                count = 0
                color = 0

                for x in range(5):

                    r, g, b = im.getpixel((j, i))

                    r_total += r
                    g_total += g
                    b_total += b
                    count += 1
                    c_pixel += 1
                    #print((x, y), (j+x, i+y))

                    color = (r_total//5, g_total//5, b_total//5)
                    r_a = r_total//5
                    g_t = g_total//5
                    b_t = b_total//5

        # newImage[i].append(color)

            if color == (0, 0, 0):
                newImage[i].append(pared)
            elif (g_t > b_t > r_a):
                newImage[i].append(meta)
            elif(r_a > g_t) and (r_a > b_t):
                newImage[i].append(inicio)
            elif color == (255, 255, 255):
                newImage[i].append(terreno)
            elif color == (76, 76, 76):
                newImage[i].append(pared)
            elif (r_a == g_t == b_t) and (r_a, g_t, b_t != 255):
                newImage[i].append(pared)
            elif color == (253, 253, 253):
                newImage[i].append(pared)
            elif color == (254, 254, 254):
                newImage[i].append(pared)
            elif color == (255, 255, 255):
                newImage[i].append(pared)
            elif color == (255, 255, 255):
                newImage[i].append(pared)
            else:
                newImage[i].append(terreno)

    ims = np.asarray(newImage)

    cv2.imwrite('maze.png', ims)
    return ('maze.png')
