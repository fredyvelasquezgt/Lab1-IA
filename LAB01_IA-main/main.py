import Astar
import BFS
import AlDFS
import DisImage


filename = '2.bmp'
maze = DisImage.RenderImage(filename)

Astar.Astar(maze)
BFS.main(maze)
start_x, start_y, end_x, end_y = Astar.Astar(maze)
AlDFS.DFSm(maze, start_x, start_y, end_x, end_y)
