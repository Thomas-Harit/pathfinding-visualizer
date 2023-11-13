from tkinter import Frame
from cell import Cell
from generation import generate_maze
from solver import solve
import random


class Maze(Frame):
    def __init__(self, app, size_x=15, size_y=15, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app

        self.config(bg="white")
        self.size_x = size_x
        self.size_y = size_y

        self.cells: dict[(int, int), Cell] = {}
        self.start: Cell = None
        self.goal: Cell = None

        for i in range(size_y):
            self.grid_rowconfigure(i, weight=1)
            for j in range(size_x):
                self.grid_columnconfigure(j, weight=1)
                self.cells[(j, i)] = Cell(self.app, j, i, master=self)

    def pack(self, **kwargs):
        super().pack(fill="both", expand=1, **kwargs)
        for cell in self.cells.values():
            cell.pack()

    def generate(self):
        # Generate the maze
        maze = generate_maze(self.size_x, self.size_y)

        # Set paths and walls cells
        for i in range(self.size_y):
            for j in range(self.size_x):
                if maze[i][j] == 0:
                    self.cells[(j, i)].make_path()
                else:
                    self.cells[(j, i)].make_wall()

        # Randomly choose start and goal
        paths = self.paths()

        self.start = random.choice(paths)
        self.start.make_start()
        while (self.goal == None or self.goal == self.start):
            self.goal = random.choice(paths)
        self.goal.make_goal()

    def clear(self):
        for cell in self.cells.values():
            cell.make_path()
        self.start = None
        self.goal = None

    def neighbours(self, cell: Cell):
        neighbours = []
        x, y = cell.pos
        neighbours_pos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for pos in neighbours_pos:
            if pos in self.cells and self.cells[pos].is_wall == False:
                neighbours.append(self.cells[pos])

        return neighbours

    def paths(self):
        paths = []

        for cell in self.cells.values():
            if cell.is_wall == False:
                paths.append(cell)

        return paths

    def walls(self):
        walls = []

        for cell in self.cells.values():
            if cell.is_wall == True:
                walls.append(cell)

        return walls

    def solve(self, path_to_walk: list[tuple[int, int]] = None):
        if (self.start == None or self.goal == None):
            return
        path_to_walk = solve(self)

        for pos in path_to_walk:
            if (pos == self.start.pos or pos == self.goal.pos):
                continue
            self.cells[pos].make_walked()
