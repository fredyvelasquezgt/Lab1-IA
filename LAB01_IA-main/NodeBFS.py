"""
Coordinate Class to be used in implementing BFS
Provides Information about:
    -Location ([y][x])
    -Who is Parent (Another Coordinate)
    -Is Goal (bool)
"""


class Coordinate:

    def __init__(self, y: int, x: int, parent):
        self.y = y
        self.x = x
        self.parent = parent

        if self.parent is not None:
            self.count = parent.count + 1
        else:
            self.count = 0

    # add in 'step count' attribute that counts length of path using parent step +1
    # decide on shortest route by comparing step counts at end, if new path is shorter, change goal node parent to new path
