from PIL import Image

"""
Module to handle the conversions between a list of lists of strings (Matrix) and an Image (from PIL)
Matrix acesses data values through data[row,column] format
Define Functions for:
    -Converting Image to Matrix (and vv)                [  ]
    -Converting Color(tuple) to Symbol(str) (and vv)    [v/]
    -Printing out a Matrix                              [v/]
"""

hgt, wid = 1, 1


def imgToMatrix(img: Image) -> list:
    data = img.load()
    global hgt, wid
    hgt, wid = img.height, img.width
    outMat = [[pixToSym(data[y, x]) for x in range(img.width)]
              for y in range(img.height)]
    return outMat


def matrixToImg(mat: list) -> Image:
    outImg = Image.new(mode="RGBA", size=(wid, hgt))
    data = outImg.load()
    for y in range(outImg.height):
        for x in range(outImg.width):
            data[y, x] = symToPix(mat[y][x])
    return outImg


def pixToSym(col: tuple) -> str:
    if col == (0, 0, 0, 255):
        return 'B'
    elif col == (255, 255, 255, 255):
        return '0'
    elif col == (0, 0, 255, 255):
        return 'S'
    elif col == (0, 255, 0, 255):
        return 'F'
    else:
        raise Exception("Unrecognized Color Value: "+str(col))


def symToPix(sym: str) -> tuple:
    if sym == 'B':
        return (0, 0, 0, 255)
    elif sym == '0':
        return (255, 255, 255, 255)
    elif sym == 'S':
        return (0, 0, 255, 255)
    elif sym == 'F':
        return (0, 255, 0, 255)
    elif sym == 'A':
        return (175, 119, 181, 255)
    elif sym == 'P':
        return (77, 163, 46, 255)
    else:
        raise Exception("Unrecognized Symbol Value: \'"+str(sym)+"\'")


def printMatrix(mat: list):
    for y in range(len(mat)):
        print(''.join(mat[y][x] for x in range(len(mat[0]))))
