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
        return model(x, y, z, phi, tetha, psi, P4, m, L, dt, k11, k22, k33, k14, k25, k36)

def model(x0, y0, z0, phi0, theta0, psi0, P4, m, L, dt, k11, k22, k33, k14, k25, k36):
    V0 = np.array([x0, y0, z0, 0.0, 0.0, 0.0, phi0, theta0, psi0, 0.0, 0.0, 0.0]).transpose()

    def func(t, V):
        g = 9.8
        x, y, z, vx, vy, vz, phi, theta, psi, Wx, Wy, Wz = V

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

        u = K @ V + K1 @ V

        P1 = P4 - (u[1] + u[2]) / 2
        P2 = P4 - (u[0] + u[1]) / 2
        P3 = P4 - (u[0] + u[2]) / 2

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

    res = solve_ivp(func, [0, 20], V0, max_step=dt)
    return res.t, res.y
