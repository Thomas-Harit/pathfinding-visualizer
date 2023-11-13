import random


def generate_maze(width, height):
    # Create a grid with all walls initially.
    maze = [[1 for _ in range(width)] for _ in range(height)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height

    def get_neighbors(x, y):
        neighbors = [(x - 2, y), (x + 2, y), (x, y - 2), (x, y + 2)]
        random.shuffle(neighbors)  # Randomly shuffle the order of neighbors.
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]

    def carve_path(x, y):
        maze[y][x] = 0  # Carve the current cell
        neighbors = get_neighbors(x, y)

        for nx, ny in neighbors:
            if maze[ny][nx] == 1:
                # Carve a passage between the current cell and the chosen neighbor.
                maze[(ny + y) // 2][(nx + x) // 2] = 0
                carve_path(nx, ny)  # Recursively visit the neighbor.

    # Start the maze generation from a random cell.
    start_x, start_y = random.randrange(
        1, width, 2), random.randrange(1, height, 2)
    carve_path(start_x, start_y)

    return maze
