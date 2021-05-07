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

        frame_ax = tk.Frame(frame)
        frame_ax.place(relheight=0.95, relwidth=0.65, relx=0.33, rely=0.02)
        self._create_ax(frame_ax)

        frame_buttons = tk.Frame(frame, bg="gray94")
        frame_buttons.place(relheight=0.1, relwidth=0.29, relx=0.02, rely=0.9)
        self._create_buttons(frame_buttons)

        frame_graphic_radio = tk.LabelFrame(frame, bg="gray94", text='Graphics')
        frame_graphic_radio.place(relheight=0.3, relwidth=0.27, relx=0.03, rely=0.55)
        self._create_graphics_selection_buttons(frame_graphic_radio)

    def _create_graphics_selection_buttons(self, master):
        self.view.var_graphic = tk.StringVar()
        self.view.var_graphic.set("coords")

        radio_coords = tk.Radiobutton(master, text="Coords", font=15,
            variable=self.view.var_graphic, value="coords", padx=10, pady=5)
        radio_coords.place(relx=0.01, rely=0.03)

        radio_speeds = tk.Radiobutton(master, text="Speeds", font=15,
            variable=self.view.var_graphic, value="speeds", padx=10, pady=5)
        radio_speeds.place(relx=0.01, rely=0.33)

        radio_angles = tk.Radiobutton(master, text="Angles", font=15,
            variable=self.view.var_graphic, value="angles", padx=10, pady=5)
        radio_angles.place(relx=0.01, rely=0.63)

        radio_angle_speeds = tk.Radiobutton(master, text="Angle speeds", font=15,
            variable=self.view.var_graphic, value="angle_speeds", padx=10, pady=5)
        radio_angle_speeds.place(relx=0.41, rely=0.03)

        radio_voltage = tk.Radiobutton(master, text="Voltage", font=15,
            variable=self.view.var_graphic, value="voltage", padx=10, pady=5)
        radio_voltage.place(relx=0.41, rely=0.33)

        radio_power = tk.Radiobutton(master, text="Power", font=15,
            variable=self.view.var_graphic, value="power", padx=10, pady=5)
        radio_power.place(relx=0.41, rely=0.63)

    def _create_ax(self, master):
        fig = plt.figure()
        self.view.ax = fig.add_subplot(111)
        self.view._create_ax()
        self.view.canvas = FigureCanvasTkAgg(fig, master)
        self.view.canvas.get_tk_widget().pack(fill=tk.BOTH)
        self.view.canvas.draw()

    def _create_buttons(self, master):
        self.view.button_start = tk.Button(master, text="Start", font=15, bg="white",
                                           command=self.view._click_button_start)
        self.view.button_start.place(relwidth=0.3, relx=0.0)

        self.view.button_stop = tk.Button(master, text="Stop", font=15, bg="white",
                                          command=self.view._click_button_stop, state=tk.DISABLED)
        self.view.button_stop.place(relwidth=0.3, relx=0.33)

        self.view.button_show = tk.Button(master, text="Show", font=15, bg="white",
                                          command=self.view._click_show_result, state=tk.DISABLED)
        self.view.button_show.place(relwidth=0.3, relx=0.66)


class StabilizationForm:

    def __init__(self, view, frame):
        self.view = view
        self._create_widgets(frame)

    def _create_widgets(self, frame):
        # параметры
        self.view.var_k11 = tk.StringVar()
        self.view.var_k22 = tk.StringVar()
        self.view.var_k33 = tk.StringVar()
        self.view.var_k14 = tk.StringVar()
        self.view.var_k25 = tk.StringVar()
        self.view.var_k36 = tk.StringVar()

        stabilization_frame = ttk.LabelFrame(frame, text='Stabilization matrix')
        stabilization_frame.place(relheight=0.8, relwidth=0.77, relx=0.02, rely=0.1)

        tk.Label(stabilization_frame, text='k11 =', font=15).grid(
            row=0, column=0, padx=5, pady=5, sticky='wn')
        tk.Entry(stabilization_frame, textvariable=self.view.var_k11, font=15, width=8).grid(
            row=0, column=1)

        tk.Label(stabilization_frame, text='k22 =', font=15).grid(
            row=1, column=2)
        tk.Entry(stabilization_frame, textvariable=self.view.var_k22, font=15, width=8).grid(
            row=1, column=3)

        tk.Label(stabilization_frame, text='k33 =', font=15).grid(
            row=2, column=4)
        tk.Entry(stabilization_frame, textvariable=self.view.var_k33, font=15, width=8).grid(
            row=2, column=5)

        tk.Label(stabilization_frame, text='k14 =', font=15).grid(
            row=0, column=6)
        tk.Entry(stabilization_frame, textvariable=self.view.var_k14, font=15, width=8).grid(
            row=0, column=7)

        tk.Label(stabilization_frame, text='k25 =', font=15).grid(
            row=1, column=8)
        tk.Entry(stabilization_frame, textvariable=self.view.var_k25, font=15, width=8).grid(
            row=1, column=9)

        tk.Label(stabilization_frame, text='k36 =', font=15).grid(
            row=2, column=10, padx=5, pady=5, sticky='se')
        tk.Entry(stabilization_frame, textvariable=self.view.var_k36, font=15, width=8).grid(
            row=2, column=11)


class ParamsForm:
    def __init__(self, view, frame):
        self.view = view
        self._create_widgets(frame)

    def _create_widgets(self, frame):

        # Объявление переменных
        self.view.var_x = tk.StringVar()
        self.view.var_y = tk.StringVar()
        self.view.var_z = tk.StringVar()
        self.view.var_phi = tk.StringVar()
        self.view.var_tetha = tk.StringVar()
        self.view.var_psi = tk.StringVar()
        self.view.var_P4 = tk.StringVar()
        self.view.var_m = tk.StringVar()
        self.view.var_L = tk.StringVar()
        self.view.var_dt = tk.StringVar()

        initial_frame = ttk.LabelFrame(frame, text='Initial conditions')
        initial_frame.place(relheight=0.8, relwidth=0.77, relx=0.02, rely=0.1)

        #phi, tetha, psi

        tk.Label(initial_frame, text='phi =', font=15).grid(
            row=0, column=0, padx=15, pady=5, sticky='wn')
        tk.Entry(initial_frame, textvariable=self.view.var_phi, font=15, width=12).grid(
            row=0, column=1)

        tk.Label(initial_frame, text='theta =', font=15).grid(
            row=1, column=0)
        tk.Entry(initial_frame, textvariable=self.view.var_tetha, font=15, width=12).grid(
            row=1, column=1)

        tk.Label(initial_frame, text='psi =', font=15).grid(
            row=2, column=0, padx=15, pady=5, sticky='se')
        tk.Entry(initial_frame, textvariable=self.view.var_psi, font=15, width=12).grid(
            row=2, column=1)

        # x y z

        tk.Label(initial_frame, text='x =', font=15).grid(
            row=0, column=2, padx=15, pady=5, sticky='wn')
        tk.Entry(initial_frame, textvariable=self.view.var_x, font=15, width=12).grid(
            row=0, column=3)

        tk.Label(initial_frame, text='y =', font=15).grid(
            row=1, column=2)
        tk.Entry(initial_frame, textvariable=self.view.var_y, font=15, width=12).grid(
            row=1, column=3)

        tk.Label(initial_frame, text='z =', font=15).grid(
            row=2, column=2, padx=15, pady=5, sticky='se')
        tk.Entry(initial_frame, textvariable=self.view.var_z, font=15, width=12).grid(
            row=2, column=3)

        # P4 m L

        tk.Label(initial_frame, text='P4 =', font=15).grid(
            row=0, column=4, padx=15, pady=5, sticky='wn')
        tk.Entry(initial_frame, textvariable=self.view.var_P4, font=15, width=12).grid(
            row=0, column=5)

        tk.Label(initial_frame, text='m =', font=15).grid(
            row=1, column=4)
        tk.Entry(initial_frame, textvariable=self.view.var_m, font=15, width=12).grid(
            row=1, column=5)

        tk.Label(initial_frame, text='L =', font=15).grid(
            row=2, column=4, padx=15, pady=5, sticky='se')
        tk.Entry(initial_frame, textvariable=self.view.var_L, font=15, width=12).grid(
            row=2, column=5)

        # dt

        tk.Label(initial_frame, text='dt =', font=15).grid(
            row=0, column=6, padx=15, pady=5, sticky='se')
        tk.Entry(initial_frame, textvariable=self.view.var_dt, font=15, width=12).grid(
            row=0, column=7)


        # Костыль шоб робило
        ttk.Label(frame,
                  text="").grid(column=0, row=0, padx=65, pady=65)