import tkinter as tk
from tkinter.messagebox import showerror
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math as ma
import numpy as np
from tkinter import ttk
from widgets import Widgets
from widgets import StabilizationForm
from widgets import ParamsForm

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

        self._create_tabs()

        frame.pack()

        widgets = Widgets(self, frame)
        self._set_default_values


    def _set_default_values(self):
        self.var_k11.set(-1.0)
        self.var_k22.set(-1.0)
        self.var_k33.set(-1.0)
        self.var_k14.set(-1.0)
        self.var_k25.set(-1.0)
        self.var_k36.set(-1.0)

        self.var_x.set(0)
        self.var_y.set(0)
        self.var_z.set(0)
        self.var_phi.set(0)
        self.var_tetha.set(0)
        self.var_psi.set(0)
        self.var_dt.set(1)

        # Для управления табами
    def _create_tabs(self):


        tabControl = ttk.Notebook(self.controller.window)

        stabilizationTab = ttk.Frame(tabControl)
        inicialTab = ttk.Frame(tabControl)

        tabControl.add(inicialTab, text='Params')
        tabControl.add(stabilizationTab, text='Stabilization')
        tabControl.pack(expand=1, fill="both")

        # Первый фрейм
        stabilization = StabilizationForm(self, stabilizationTab)

        # Второй фрейм
        params = ParamsForm(self, inicialTab)


    def _save_params(self):
        print('save params')


    def _click_button_start(self):
        try:
            self._save_params()
            self.button_start.config(state=tk.DISABLED)
            self.button_stop.config(state=tk.NORMAL)
            self.button_show.config(state=tk.DISABLED)
            print('start')
        except Exception as e:
            showerror("Error", str(e))

    def _click_button_stop(self):
        self.cancel_calculations()

    def _click_show_result(self):
        self._show_result()

    def cancel_calculations(self):
        self.controller.stop_model()
        self.button_stop.config(state=tk.DISABLED)
        self.button_start.config(state=tk.NORMAL)
        self.button_show.config(state=tk.NORMAL)

    def _create_ax(self):
        self.ax.clear()
        self.ax.grid()

    def _show_result(self):
        print('show result')