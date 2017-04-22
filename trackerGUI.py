try:
    import tkinter as tk

except ImportError:
    raise ImportError("Built using tkinter with Python 3")


class MainWindow(tk.Frame):
    def __init__(self, main):
        tk.Frame.__init__(self, main)
        self.main = main

        self.init_main_win()

    def init_main_win(self):
        self.main.title("CM's Progress Tracker")
        self.main.geometry("1000x750")







