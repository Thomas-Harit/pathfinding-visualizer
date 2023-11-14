from tkinter import Frame


class Cell(Frame):
    def __init__(self, app, pos_x, pos_y, master=None, **kwargs):
        super().__init__(master, bg="white", highlightthickness=1,
                         highlightbackground="grey", **kwargs)
        self.app = app
        self.master = master
        self.pos = (pos_x, pos_y)

        self.is_wall = False
        self.is_path = False
        self.is_goal = False
        self.is_start = False
        self.is_walked = False

        self.color = [255, 255, 255]

        self.bind("<Enter>", self.mouse_enter)
        self.bind("<Leave>", self.mouse_leave)
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)

    def pack(self, **kwargs):
        super().grid(column=self.pos[0],
                     row=self.pos[1], sticky="nsew", **kwargs)

    def make_wall(self):
        self.is_wall = True
        self.is_path = False
        self.is_goal = False
        self.is_start = False
        self.is_walked = False
        self.config(bg="gray")

    def make_path(self):
        self.is_wall = False
        self.is_path = True
        self.is_goal = False
        self.is_start = False
        self.is_walked = False
        self.config(bg="white")

    def make_start(self):
        if (self.is_goal):
            self.app.maze.goal = None
        self.make_path()
        if (self.app.maze.start != None):
            self.app.maze.start.make_path()
        self.app.maze.start = self
        self.is_start = True
        self.config(bg="green")

    def make_goal(self):
        if (self.is_start):
            self.app.maze.start = None
        self.make_path()
        if (self.app.maze.goal != None):
            self.app.maze.goal.make_path()
        self.app.maze.goal = self
        self.is_goal = True
        self.config(bg="red")

    def make_walked(self, event=None):
        self.make_path()
        self.is_walked = True
        self.config(bg="blue")

    def left_click(self, event):
        if (self.is_wall == False):
            self.make_wall()
        else:
            self.make_path()

    def right_click(self, event):
        if (self.is_goal):
            self.make_path()
        elif (self.is_start == False):
            self.make_start()
        else:
            self.make_goal()

    def mouse_enter(self, event):
        self.focus_set()

    def mouse_leave(self, event):
        self.master.focus_set()
