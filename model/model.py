import numpy as np
import copy
import random
from scipy.integrate import solve_ivp
from scipy.linalg import eig
from matplotlib import pyplot as plt
from math import sqrt
from math import sin
from math import cos


class Model:

    def __init__(self):
        self.if_cancel_computing = False

    def set_if_cancel_computing(self, if_cancel=True):
        self.if_cancel_computing = if_cancel

    def _check_to_end_computing(self):
        return self.if_cancel_computing

    def compute(self, x, y, z, phi, tetha, psi, P4, m, L, dt, k11, k22, k33, k14, k25, k36):
        return self._model(x, y, z, phi, tetha, psi, P4, m, L, dt, k11, k22, k33, k14, k25, k36)

    def _model(self, x0, y0, z0, phi0, theta0, psi0, P4, m, L, dt, k11, k22, k33, k14, k25, k36):
        V0 = np.array([x0, y0, z0, 0.0, 0.0, 0.0, phi0, theta0, psi0, 0.0, 0.0, 0.0,
                       m, L, P4, k11, k22, k33, k14, k25, k36]).transpose()

        res = solve_ivp(func, [0, 20], V0, max_step=dt)
        return res.t, res.y

def func(t, V):
    g = 9.8
    x, y, z, vx, vy, vz, phi, theta, psi, Wx, Wy, Wz, \
    m, L, P4, k11, k22, k33, k14, k25, k36 = V

    V1 = np.array([x, y, z, vx, vy, vz, phi, theta, psi, Wx, Wy, Wz]).transpose()

    # x   y     z    vx   vy   vz  ph     th   ps   wx    wy   wz
    K = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, k11, 0.0, 0.0, k14, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, k22, 0.0, 0.0, k25, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, k33, 0.0, 0.0, k36]])

    K1 = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.12445079348883241, 0.0, 0.0, -0.015556349186104051, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.12445079348883241, 0.0, 0.0, -0.015556349186104051, 0.0],
                    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.05866666666666667, 0.0, 0.0, -0.014666666666666668]])

    Ix = (m * L ** 2.0) / 6.0
    Iy = (m * L ** 2.0) / 6.0
    Iz = (m * L ** 2.0) / 3.0

    u = K @ ((1 + (0.5 - random.random())) * V1) + K1 @ ((1 + (0.5 - random.random())) * V1)

    P1 = 3 * P4 / 2 - (u[1] + u[2]) / 2
    P2 = P4 - (u[0] + u[1]) / 2
    P3 = 3 * P4 / 2 - (u[0] + u[2]) / 2

    fx = vx
    fy = vy
    fz = vz

    fvx = ((P1 + P2 + P3 + P4) / m * (sin(psi) * sin(phi) + cos(psi) * sin(theta) * cos(phi)))
    fvy = ((P1 + P2 + P3 + P4) / m * (-cos(psi) * sin(phi) + cos(phi) * sin(psi) * sin(theta)))
    fvz = ((P1 + P2 + P3 + P4) / m * (cos(theta) * cos(phi)) - g)

    fphi = Wx
    ftheta = Wy
    fpsi = Wz

    fWx = (L / sqrt(2) * u[0] - (Iz - Iy) * Wy * Wz) / (Ix)
    fWy = (L / sqrt(2) * u[1] - (Ix - Iz) * Wx * Wz) / (Iy)
    fWz = (L * u[2] - (Iy - Ix) * Wx * Wy) / (Iz)

    fV = np.array([fx, fy, fz, fvx, fvy, fvz, fphi, ftheta, fpsi, fWx, fWy, fWz]).transpose()
    return fV

# В принципе дальше идет постройка графиков, поэтому можно дальнейшее отсечь

"""t_arr, res = model(x, y, z, phi, theta, psi)

P1 = copy.deepcopy(t_arr)
P2 = copy.deepcopy(t_arr)
P3 = copy.deepcopy(t_arr)

u = K@res

i = 0

P1 = 3*P4/2 - (u[1]+u[2])/2
P2 = (P4 - (u[0]+u[1])/2)
P3 = 3*P4/2 - (u[0]+u[2])/2

fig = plt.figure()  # создаем окно с графиками

axes = fig.subplots(2, 3)

axes[0][0].plot(t_arr, P1, label="$P1$")
axes[0][0].plot(t_arr, P2, label="$P2$")
axes[0][0].plot(t_arr, P3, label="$P3$")
axes[0][0].grid()  
axes[0][0].legend()  
axes[0][0].set_xlabel("$t$")

axes[0][1].plot(t_arr, u[0], label="$Ux$")
axes[0][1].plot(t_arr, u[1], label="$Uy$")
axes[0][1].plot(t_arr, u[2], label="$Uz$")
axes[0][1].grid()  
axes[0][1].legend()  
axes[0][1].set_xlabel("$t$")

axes[0][2].plot(t_arr, res[0], label="$x$")
axes[0][2].plot(t_arr, res[1], label="$y$")
axes[0][2].plot(t_arr, res[2], label="$z$")
axes[0][2].grid()  
axes[0][2].legend()  
axes[0][2].set_xlabel("$t$")

axes[1][0].plot(t_arr, res[3], label="$Vx$")
axes[1][0].plot(t_arr, res[4], label="$Vy$")
axes[1][0].plot(t_arr, res[5], label="$Vz$")
axes[1][0].grid()  
axes[1][0].legend()  
axes[1][0].set_xlabel("$t$")

axes[1][1].plot(t_arr, res[9], label="$Wx$")
axes[1][1].plot(t_arr, res[10], label="$Wy$")
axes[1][1].plot(t_arr, res[11], label="$Wz$")
axes[1][1].grid()  
axes[1][1].legend()  
axes[1][1].set_xlabel("$t$")

axes[1][2].plot(t_arr, res[6], label="$Phi$")
axes[1][2].plot(t_arr, res[7], label="$Theta$")
axes[1][2].plot(t_arr, res[8], label="$Psi$")
axes[1][2].grid()  
axes[1][2].legend()  
axes[1][2].set_xlabel("$t$")

fig.tight_layout()

plt.show()"""
