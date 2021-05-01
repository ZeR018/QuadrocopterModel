import tkinter as tk
from tkinter.messagebox import showerror
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as ma
import numpy as np
from tkinter import ttk
from widgets import Widgets

#from widgets import Widgets


class View:

    def __init__(self, controller):
        self.controller = controller
        self._create_window()

    def _create_window(self):
        window = self.controller.window

        # Для изменения заголовка окна
        window.title('Quadrocopter')

        self._create_tabs()

        # Для изменения размеров окна wsize
        wsize = (1000, 600)

        window.geometry('%dx%d' % wsize)
        window.resizable(width=False, height=False)

        # Для изменения БГ окна
        frame = tk.Frame(window, bg='gray94', width=wsize[0], height=wsize[1])
        frame.pack()

        widgets = Widgets(self, frame)

        # Для управления табами
    def _create_tabs(self):
        tabControl = ttk.Notebook(self.controller.window)

        stabilizationTab = ttk.Frame(tabControl)
        inicialTab = ttk.Frame(tabControl)

        tabControl.add(inicialTab, text='Params')
        tabControl.add(stabilizationTab, text='Stabilization')
        tabControl.pack(expand=1, fill="both")

        # Первый фрейм
        stabilization_frame = ttk.LabelFrame(stabilizationTab, text='Stabilization matrix')
        stabilization_frame.place(relheight=0.8, relwidth=0.77, relx=0.02, rely=0.1)

        tk.Label(stabilization_frame, text='k11 =', font=15).grid(
            row=0, column=0, padx=5, pady=5, sticky='wn')
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=0, column=1)

        tk.Label(stabilization_frame, text='k22 =', font=15).grid(
            row=1, column=2)
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=1, column=3)

        tk.Label(stabilization_frame, text='k33 =', font=15).grid(
            row=2, column=4)
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=2, column=5)

        tk.Label(stabilization_frame, text='k14 =', font=15).grid(
            row=0, column=6)
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=0, column=7)

        tk.Label(stabilization_frame, text='k25 =', font=15).grid(
            row=1, column=8)
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=1, column=9)

        tk.Label(stabilization_frame, text='k36 =', font=15).grid(
            row=2, column=10, padx=5, pady=5, sticky='se')
        tk.Entry(stabilization_frame, font=15, width=8).grid(
            row=2, column=11)

        # Второй фрейм
        initial_frame = ttk.LabelFrame(inicialTab, text='Initial conditions')
        initial_frame.place(relheight=0.8, relwidth=0.77, relx=0.02, rely=0.1)

        tk.Label(initial_frame, text='Рыскание =', font=15).grid(
            row=0, column=0, padx=5, pady=5, sticky='wn')
        tk.Entry(initial_frame, font=15, width=8).grid(
            row=0, column=1)

        tk.Label(initial_frame, text='Тангаж =', font=15).grid(
            row=1, column=0)
        tk.Entry(initial_frame, font=15, width=8).grid(
            row=1, column=1)

        tk.Label(initial_frame, text='Крен =', font=15).grid(
            row=2, column=0, padx=5, pady=5, sticky='se')
        tk.Entry(initial_frame, font=15, width=8).grid(
            row=2, column=1)


        # Костыль шоб робило
        ttk.Label(inicialTab,
                  text="").grid(column=0, row=0, padx=65, pady=65)

    def _create_ax(self):
        self.ax.clear()
        self.ax.grid()
