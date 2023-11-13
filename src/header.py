from tkinter import Frame, Label


class Header(Frame):
    def __init__(self, app, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.app = app

        self.config(bg="black", borderwidth=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.generate_label = Label(self, text="Generate", fg="white",
                                    bg="black", font=("Arial", 20), cursor="hand2")
        self.clear_label = Label(self, text="Clear", fg="white",
                                 bg="black", font=("Arial", 20), cursor="hand2")
        self.solve_label = Label(self, text="Solve", fg="white",
                                 bg="black", font=("Arial", 20), cursor="hand2")

        self.generate_label.bind("<Button-1>", self.click_generate)
        self.generate_label.bind("<Enter>", self.mouse_enter_generate)
        self.generate_label.bind("<Leave>", self.mouse_leave_generate)

        self.clear_label.bind("<Button-1>", self.click_clear)
        self.clear_label.bind("<Enter>", self.mouse_enter_clear)
        self.clear_label.bind("<Leave>", self.mouse_leave_clear)

        self.solve_label.bind("<Button-1>", self.click_solve)
        self.solve_label.bind("<Enter>", self.mouse_enter_solve)
        self.solve_label.bind("<Leave>", self.mouse_leave_solve)

    def pack(self, **kwargs):
        super().pack(**kwargs)
        self.clear_label.grid(column=0, row=0, sticky="nsew")
        self.generate_label.grid(column=1, row=0, sticky="nsew")
        self.solve_label.grid(column=2, row=0, sticky="nsew")

    def click_generate(self, event):
        self.app.maze.generate()

    def click_clear(self, event):
        self.app.maze.clear()

    def click_solve(self, event):
        self.app.maze.solve()

    def mouse_enter_generate(self, event):
        self.generate_label.config(fg=f"#{128:2x}{128:2x}{128:2x}")

    def mouse_leave_generate(self, event):
        self.generate_label.config(fg="white")

    def mouse_enter_clear(self, event):
        self.clear_label.config(fg=f"#{128:2x}{128:2x}{128:2x}")

    def mouse_leave_clear(self, event):
        self.clear_label.config(fg="white")

    def mouse_enter_solve(self, event):
        self.solve_label.config(fg=f"#{128:2x}{128:2x}{128:2x}")

    def mouse_leave_solve(self, event):
        self.solve_label.config(fg="white")
