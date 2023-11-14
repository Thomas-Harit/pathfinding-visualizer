import sys

sys.path.append("src")

from tkinter import Tk
from header import Header
from maze import Maze


class App:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.minsize(640, 720)
        self.root.title("Frame Example")

        # Create the main window
        self.header = Header(self, self.root)
        self.header.pack(fill="x")

        self.maze = Maze(self, master=self.root)
        self.maze.pack()

    def loop(self) -> None:
        self.root.mainloop()


app = App()

app.loop()
