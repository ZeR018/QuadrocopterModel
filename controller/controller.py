from tkinter import Tk
import threading

from view import View
from model import Model

class Controller:

    def __init__(self):
        self.window = Tk()

        def on_close():
            self.window.quit()
            self.window.destroy()

        self.window.protocol('WM_DELETE_WINDOW', on_close)

        self.view = View(self)
        self.result = None
        self.graphic = None
        self.model = None


    def run(self):
        self.window.mainloop()

    def start_model(self, stabilization_params, initial_params):
        x, y, z, phi, tetha, psi, P4, m, L, dt = initial_params
        k11, k22, k33, k14, k25, k36 = stabilization_params

        def run_thread():
            self.model = Model()
            self.result = self.model.compute(x, y, z, phi, tetha, psi, P4, m, L, dt, k11, k22, k33, k14, k25, k36)
            self.view.cancel_calculations()

        self.thread = threading.Thread(target=run_thread)
        self.thread.start()

    def stop_model(self):
        if self.model:
            self.model.set_if_cancel_computing(True)

