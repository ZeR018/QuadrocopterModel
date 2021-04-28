import tkinter as tk
from tkinter.messagebox import showerror
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as ma
import numpy as np
from tkinter import ttk

#from widgets import Widgets


class View:

    def __init__(self, controller):
        self.controller = controller
        self._create_window()

    def _create_window(self):
        window = self.controller.window

        # Для изменения заголовка окна
        window.title('Quadrocopter')


        # Для изменения размеров окна wsize
        wsize = (1000, 600)

        window.geometry('%dx%d' % wsize)
        window.resizable(width=False, height=False)

        # Для изменения БГ окна
        frame = tk.Frame(window, bg='gray94', width=wsize[0], height=wsize[1])
        frame.pack()

        # Несколько вкладок
        tabControl = ttk.Notebook(window)

        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Tab 1')
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1, fill="both")

        ttk.Label(tab1,
                  text="Welcome to \
                  GeeksForGeeks").grid(column=0,
                                       row=0,
                                       padx=30,
                                       pady=30)
        ttk.Label(tab2,
                  text="Lets dive into the\
                  world of computers").grid(column=0,
                                            row=0,
                                            padx=30,
                                            pady=30)


