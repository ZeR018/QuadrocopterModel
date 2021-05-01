from tkinter import Tk
import threading

from view import View

class Controller:

    def __init__(self):
        self.window = Tk()

        def on_close():
            self.window.quit()
            self.window.destroy()

        self.window.protocol('WM_DELETE_WINDOW', on_close)

        self.view = View(self)


    def run(self):
        self.window.mainloop()
