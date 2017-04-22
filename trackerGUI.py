try:
    import tkinter as tk

except ImportError:
    raise ImportError("Built using tkinter with Python 3")


class MainWindow(tk.Frame):
    def __init__(self, main):
        tk.Frame.__init__(self, main)
        self.main = main
        self.top_left_frame = tk.Frame(main, background="bisque")  # Colours for development purposes
        self.top_right_frame = tk.Frame(main, background="pink")
        self.bottom_left_frame = tk.Frame(main, background="blue")
        self.bottom_right_frame = tk.Frame(main, background="green")

        # Widgets
        self.main_label = tk.Label(self.top_left_frame, text="Main Label")

        self.date_label = tk.Label(self.bottom_left_frame, text="Enter Date (dd/mm/yyyy):")
        self.date_entry = tk.Entry(self.bottom_left_frame)

        self.squat_label = tk.Label(self.bottom_left_frame, text="Enter Squat (kg): ")
        self.squat_entry = tk.Entry(self.bottom_left_frame)

        self.bench_label = tk.Label(self.bottom_left_frame, text="Enter Bench Press (kg): ")
        self.bench_entry = tk.Entry(self.bottom_left_frame)

        self.deadlift_label = tk.Label(self.bottom_left_frame, text="Enter Deadlift (kg): ")
        self.deadlift_entry = tk.Entry(self.bottom_left_frame)

        self.change_previous = tk.Button(self.bottom_left_frame, text="Update previous submission")
        self.update = tk.Button(self.bottom_left_frame, text="Update")

        self.total_label = tk.Label(self.top_right_frame, text="Current Best Total = XXX kg")

        self.temp_graph_widget = tk.Label(self.bottom_right_frame, text="[GRAPH GOES HERE]")

        self.init_main_win()

    def init_main_win(self):
        self.main.title("CM's Progress Tracker")
        self.main.geometry("1000x750")

        # LAYOUT

        # Configure main frame
        for row in range(0, 2):
            self.main.grid_rowconfigure(row, weight=1)

        for col in range(0, 4):
            self.main.grid_columnconfigure(col, weight=1)

        # Configure top frames
        for row, col in zip(range(0, 3), range(0, 3)):
            self.top_left_frame.grid_rowconfigure(row, weight=1)
            self.top_left_frame.grid_columnconfigure(col, weight=1)
            self.top_right_frame.grid_rowconfigure(row, weight=1)
            self.top_right_frame.grid_columnconfigure(col, weight=1)

        self.main_label.grid(row=1, column=1, sticky="nesw")
        self.total_label.grid(row=1, column=1, sticky="nesw")

        # Configure bottom-left frame
        for row in range(0, 11):
            self.bottom_left_frame.grid_rowconfigure(row, weight=1)

        self.date_label.grid(row=1, column=1, columnspan=2, sticky="nesw")
        self.date_entry.grid(row=1, column=3, sticky="nesw")
        self.squat_label.grid(row=2, column=1, columnspan=2, sticky="nesw")
        self.squat_entry.grid(row=2, column=3, sticky="nesw")
        self.bench_label.grid(row=3, column=1, columnspan=2, sticky="nesw")
        self.bench_entry.grid(row=3, column=3, sticky="nesw")
        self.deadlift_label.grid(row=4, column=1, columnspan=2, sticky="nesw")
        self.deadlift_entry.grid(row=4, column=3, sticky="nesw")

        self.change_previous.grid(row=6, column=1, sticky="nesw")
        self.update.grid(row=6, column=3, sticky="nesw")

        for col in range(0, 5):
            self.bottom_left_frame.grid_columnconfigure(col, weight=1)

        # Bottom-right frame
        self.temp_graph_widget.pack(expand=1)

        self.top_left_frame.grid(row=0, column=0, sticky="nesw")
        self.top_right_frame.grid(row=0, column=1, columnspan=3, sticky="nesw")
        self.bottom_left_frame.grid(row=1, column=0, sticky="nesw")
        self.bottom_right_frame.grid(row=1, column=1, columnspan=3, sticky="nesw")
