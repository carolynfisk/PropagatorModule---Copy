#learning how to use odeint

import scipy
import numpy as np

def pend(y,t):
    theta, omega = y
    b = .25
    c=5
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return(dydt)



y0 = [np.pi - 1, 0]
#t= np.linspace(0,10,101)
t = np.linspace(0, 10, 101)
from scipy.integrate import odeint
sol = odeint(pend,y0,t)

"""
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
"""
