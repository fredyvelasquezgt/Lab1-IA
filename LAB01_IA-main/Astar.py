import NodesAs as ng
import time
import ImageReaderAstar
import DisImage
# Basado en : https://github.com/mralwaleed/maze-solving


def Astar(file):

    image_to_process = file
    image_to_save = 'ResultadoAstar.bmp'

    start_time = time.time()

    print("Reading image")
    matrix, (start_x, start_y), (end_x,
                                 end_y) = ImageReaderAstar.read_image(image_to_process)
    print(start_x, start_y)
    print(end_x, end_y)
    print("Setting nodes")
    node_grid = ng.NodeGrid(matrix)
    node_grid.set_start(start_x, start_y)
    node_grid.set_end(end_x, end_y)

    print("Finding path")
    path = node_grid.find_path()

    print("Path found")
    print("Drawing path")
    ImageReaderAstar.draw_path(image_to_process, image_to_save, path)

    print("Finished")

    return (start_x, start_y, end_x, end_y)
