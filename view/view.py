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
        self._set_default_values()


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
        self.var_phi.set(-15.0)
        self.var_tetha.set(30.0)
        self.var_psi.set(10.0)
        self.var_dt.set(0.1)
        self.var_P4.set(2.0)
        self.var_m.set(0.055)
        self.var_L.set(0.05)

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

    def _get_initial_params(self):
        try: x = float(self.var_x.get())
        except Exception: raise Exception("Variable 'x' should be float")
        try: y = float(self.var_y.get())
        except Exception: raise Exception("Variable 'y' should be float")
        try: z = float(self.var_z.get())
        except Exception: raise Exception("Variable 'z' should be float")

        try: phi = float(self.var_phi.get())
        except Exception: raise Exception("Variable 'phi' should be float")
        try: tetha = float(self.var_tetha.get())
        except Exception: raise Exception("Variable 'tetha' should be float")
        try: psi = float(self.var_psi.get())
        except Exception: raise Exception("Variable 'psi' should be float")

        try: P4 = float(self.var_P4.get())
        except Exception: raise Exception("Variable 'P4' should be float")

        try: m = float(self.var_m.get())
        except Exception: raise Exception("Variable 'm' should be float")
        if m <= 0:
            raise Exception("m should be more than 0")

        try: L = float(self.var_L.get())
        except Exception: raise Exception("Variable 'L' should be float")
        if L <= 0:
            raise Exception("L should be more than 0")

        try: dt = float(self.var_dt.get())
        except Exception: raise Exception("Variable 'dt' should be float")
        if dt <= 0:
            raise Exception("dt should be more than 0")

        return (x, y, z, phi, tetha, psi, P4, m, L, dt)

    def _get_stabilization_params(self):
        try: k11 = float(self.var_k11.get())
        except Exception: raise Exception("Variable 'k11' should be float")
        try: k22 = float(self.var_k22.get())
        except Exception: raise Exception("Variable 'k22' should be float")
        try: k33 = float(self.var_k33.get())
        except Exception: raise Exception("Variable 'k33' should be float")
        try: k14 = float(self.var_k14.get())
        except Exception: raise Exception("Variable 'k14' should be float")
        try: k25 = float(self.var_k25.get())
        except Exception: raise Exception("Variable 'k25' should be float")
        try: k36 = float(self.var_k36.get())
        except Exception: raise Exception("Variable 'k36' should be float")

        return (k11, k22, k33, k14, k25, k36)



    def _save_params(self):
        self.stabilization_params = self._get_stabilization_params()
        self.initial_params = self._get_initial_params()
        #self.graphic = self._get_graphic()


    def _click_button_start(self):
        try:
            self._save_params()
            self.button_start.config(state=tk.DISABLED)
            self.button_stop.config(state=tk.NORMAL)
            self.button_show.config(state=tk.DISABLED)
            print('start')
            self.controller.start_model(self.stabilization_params, self.initial_params)
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