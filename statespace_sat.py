import numpy as np

#using odeint to do statespace representation of satellite
#for now it has no external propagations other that the two body forces
"""
def pend(y,t,b,c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return(dydt)
"""
"""
def sat(x,t,mu):
    pos, vel = x
    x_dot = [vel, -mu*pos/(np.linalg.norm(pos))**3]
    return(x_dot)
"""
def sat(state, t):
    #x = np.array(pos,vel)
    pos= state[0:3]
    vel = state[3:6]
    mu = 3.986*10**14

    pos_dot = vel
    vel_dot = -mu*pos/(np.linalg.norm(pos))**3

    state_dot = np.concatenate((pos_dot, vel_dot))
    return(state_dot)

#mu = 3.986*10**14

state0 = np.array([4177.910263, 653.273287, 5210.486080,-0.147450, 7.671181, -0.843558])
"""
pos0 = np.array([4177.910263, 653.273287, 5210.486080])
vel0 = np.array([-0.147450, 7.671181, -0.843558])

x0 = [pos0,vel0]
"""
#t= np.linspace(0,10,101)

t= np.linspace(0,1,10)

from scipy.integrate import odeint
#x_dot = sat(x,t,mu)
sol = odeint(sat,state0,t)
#get a warning

#helpful: pdb.run('statespace_sat')
#debuggers
