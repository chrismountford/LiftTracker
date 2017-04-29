import MySQLConn
import Plots
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import tkinter as tk
from tkinter import font


class MainWindow(tk.Frame):  # TODO: Update window issue - I think it needs to be its own class
    def __init__(self, main):
        tk.Frame.__init__(self, main)
        self.main = main

        bg_col = "snow"
        fg_col = "steel blue"
        main_label_font = tk.font.Font(family="Helvetica", size=20, weight="bold")
        total_font = tk.font.Font(family="Helvetica", size=20)
        other_labels_font = tk.font.Font(family="Helvetica", size=12)

        self.top_left_frame = tk.Frame(main, background=bg_col)
        self.top_right_frame = tk.Frame(main, background=bg_col)
        self.bottom_left_frame = tk.Frame(main, background=bg_col)
        self.bottom_right_frame = tk.Frame(main, background=bg_col)

        # Widgets
        self.main_label = tk.Label(self.top_left_frame, text="Progress Tracker",
                                   background=bg_col, foreground=fg_col, font=main_label_font)

        self.date_label = tk.Label(self.bottom_left_frame, text="Enter Date (yyyy-mm-dd):",
                                   background=bg_col, foreground=fg_col, font=other_labels_font)
        self.date_entry = tk.Entry(self.bottom_left_frame, background=bg_col, foreground=fg_col)

        self.squat_label = tk.Label(self.bottom_left_frame, text="Enter Squat (kg): ",
                                    background=bg_col, foreground=fg_col, font=other_labels_font)
        self.squat_entry = tk.Entry(self.bottom_left_frame, background=bg_col, foreground=fg_col)

        self.bench_label = tk.Label(self.bottom_left_frame, text="Enter Bench Press (kg): ",
                                    background=bg_col, foreground=fg_col, font=other_labels_font)
        self.bench_entry = tk.Entry(self.bottom_left_frame, background=bg_col, foreground=fg_col)

        self.deadlift_label = tk.Label(self.bottom_left_frame, text="Enter Deadlift (kg): ",
                                       background=bg_col, foreground=fg_col, font=other_labels_font)
        self.deadlift_entry = tk.Entry(self.bottom_left_frame, background=bg_col, foreground=fg_col)

        self.change_previous = tk.Button(self.bottom_left_frame, text="Update Previous Submission", background="cadetblue1",
                                         command=lambda: self.create_window())
        self.update = tk.Button(self.bottom_left_frame, text="Update", background="steelblue1",
                                command=lambda: combine_funcs(self.update_db(), self.clear_entry_text(),
                                                              self.total_updater(), self.graph_refresher()))

        self.total_text = tk.StringVar()
        self.total_text = "Current Best Total:\n{} kg"  # TODO: Maybe also calculate wilks?
        self.total_label = tk.Label(self.top_right_frame, text=self.total_text.format(MySQLConn.return_best_total()),
                                    background=bg_col, foreground=fg_col, font=total_font)

        self.date_picked_value = tk.StringVar()  # For use in update submission window

        self.f = Figure(figsize=(5, 4), dpi=100)
        self.subplot = self.f.add_subplot(111)

        self.squat_line, = self.subplot.plot(Plots.dates_for_graph(), Plots.squats_for_graph())  # Comma turns these into tuples
        self.bench_line, = self.subplot.plot(Plots.dates_for_graph(), Plots.benchs_for_graph())
        self.dead_line, = self.subplot.plot(Plots.dates_for_graph(), Plots.deads_for_graph())

        self.f.legend(loc="upper left", handles=[self.squat_line, self.bench_line, self.dead_line],
                      labels=['Squat (kg)', 'Bench (kg)', 'Deadlift (kg'])

        self.subplot.set_ylim(min(Plots.all_lifts)-50, max(Plots.all_lifts)+50)

        self.canvas = FigureCanvasTkAgg(self.f, self.bottom_right_frame)

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
        # self.temp_graph_widget.pack(expand=1)
        self.canvas.get_tk_widget().pack(expand=1)

        self.top_left_frame.grid(row=0, column=0, sticky="nesw")
        self.top_right_frame.grid(row=0, column=1, columnspan=3, sticky="nesw")
        self.bottom_left_frame.grid(row=1, column=0, sticky="nesw")
        self.bottom_right_frame.grid(row=1, column=1, columnspan=3, sticky="nesw")

    def update_db(self):
        date_entered = self.date_entry.get()
        squat_entered = self.squat_entry.get()
        bench_entered = self.bench_entry.get()
        deadlift_entered = self.deadlift_entry.get()

        MySQLConn.conn_update(date_entered, squat_entered, bench_entered, deadlift_entered)

    def create_window(self):  # TODO: Should I rewrite this as a class?
        update_window = tk.Toplevel(self)
        update_window.wm_title("Updating Old Entry")

        update_date_label = tk.Label(update_window, text="Select a date:")
        update_date_label.grid(row=0, column=1, sticky="nesw")

        self.date_picker = ttk.Combobox(update_window, width=20, height=20)
        self.date_picker['values'] = MySQLConn.return_all_dates()
        self.date_picker.grid(row=0, column=2, sticky="nesw")

        self.date_picked_value = tk.StringVar()
        self.date_picked_value.set(self.date_picker.get())

        tk.Label(update_window, text="Squat (kg):").grid(row=1, column=0, sticky="nesw")
        tk.Label(update_window, text="Bench Press (kg):").grid(row=1, column=1, sticky="nesw")
        tk.Label(update_window, text="Deadlift (kg):").grid(row=1, column=2, sticky="nesw")

        self.squat_update_lookup = tk.StringVar()
        self.squat_update_lookup.set(value=MySQLConn.return_lift_value('squat', self.date_picked_value.get()))

        squat_update_entry = tk.Entry(update_window)
        bench_update_entry = tk.Entry(update_window)
        deadlift_update_entry = tk.Entry(update_window)

        squat_update_entry.grid(row=2, column=0, sticky="nesw")
        bench_update_entry.grid(row=2, column=1, sticky="nesw")
        deadlift_update_entry.grid(row=2, column=2, sticky="nesw")

        self.date_picker.bind("<<ComboboxSelected>>",
                              lambda x: self.date_picked_value.get())# squat_update_entry.insert(0, self.squat_update_lookup.get()))  # TODO: combine funcs for other lifts

    def clear_entry_text(self):
        self.date_entry.delete(0, 'end')
        self.squat_entry.delete(0, 'end')
        self.bench_entry.delete(0, 'end')
        self.deadlift_entry.delete(0, 'end')

    def return_values_on_combobox_event(self, value):
        return value.get()

    def total_updater(self):  # TODO: Make dependent on user
        self.total_label.config(text=self.total_text.format(MySQLConn.return_best_total()))

    def graph_refresher(self):
        self.squat_line.set_data(Plots.dates_for_graph(), Plots.squats_for_graph())
        self.bench_line.set_data(Plots.dates_for_graph(), Plots.benchs_for_graph())
        self.dead_line.set_data(Plots.dates_for_graph(), Plots.deads_for_graph())
        ax = self.canvas.figure.axes[0]
        ax.set_xlim(min(Plots.dates_for_graph()), max(Plots.dates_for_graph()))

        ax.set_ylim(min(Plots.all_lifts)-50, max(Plots.all_lifts)+50)

        self.canvas.draw()


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
