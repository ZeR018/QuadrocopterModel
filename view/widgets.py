import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


class Widgets:

    def __init__(self, view, frame):
        self.view = view
        self._create_widgets(frame)

    def _create_widgets(self, frame):

        frame_parameters = tk.LabelFrame(frame, bg="gray94", text="Parameters")
        frame_parameters.place(relheight=0.25, relwidth=0.29, relx=0.02, rely=0.2)
        self._create_parameter_entries(frame_parameters)

        frame_ax = tk.Frame(frame)
        frame_ax.place(relheight=0.95, relwidth=0.65, relx=0.33, rely=0.02)
        self._create_ax(frame_ax)

    def _create_ax(self, master):
        fig = plt.figure()
        self.view.ax = fig.add_subplot(111)
        self.view._create_ax()
        self.view.canvas = FigureCanvasTkAgg(fig, master)
        self.view.canvas.get_tk_widget().pack(fill=tk.BOTH)
        self.view.canvas.draw()

    def _create_parameter_entries(self, master):
        self.view.var_a = tk.StringVar()
        self.view.var_b = tk.StringVar()
        self.view.var_c = tk.StringVar()
        self.view.var_d = tk.StringVar()
        self.view.var_x1 = tk.StringVar()
        self.view.var_x2 = tk.StringVar()

        l_a = tk.Label(master, text="a = ", font=12)
        l_a.place(relheight=0.2, relwidth=0.15, relx=0.02, rely=0.08)
        entry_a = tk.Entry(master, textvariable=self.view.var_a, font=15)
        entry_a.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.08)

        l_b = tk.Label(master, text="b = ", font=12)
        l_b.place(relheight=0.2, relwidth=0.15, relx=0.50, rely=0.08)
        entry_b = tk.Entry(master, textvariable=self.view.var_b, font=15)
        entry_b.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.08)

        l_c = tk.Label(master, text="c = ", font=12)
        l_c.place(relheight=0.2, relwidth=0.15, relx=0.02, rely=0.38)
        entry_c = tk.Entry(master, textvariable=self.view.var_c, font=15)
        entry_c.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.38)

        l_d = tk.Label(master, text="d = ", font=12)
        l_d.place(relheight=0.2, relwidth=0.15, relx=0.50, rely=0.38)
        entry_d = tk.Entry(master, textvariable=self.view.var_d, font=15)
        entry_d.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.38)

        l_x1 = tk.Label(master, text="x1 = ", font=12)
        l_x1.place(relheight=0.2, relwidth=0.15, relx=0.009, rely=0.68)
        entry_x1 = tk.Entry(master, textvariable=self.view.var_x1, font=15)
        entry_x1.place(relheight=0.2, relwidth=0.31, relx=0.15, rely=0.68)

        l_x2 = tk.Label(master, text="x2 = ", font=12)
        l_x2.place(relheight=0.2, relwidth=0.15, relx=0.489, rely=0.68)
        entry_x2 = tk.Entry(master, textvariable=self.view.var_x2, font=15)
        entry_x2.place(relheight=0.2, relwidth=0.31, relx=0.62, rely=0.68)


