import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy as np

# --------------Initial conditions and constants-------------

totalPopulation = 195843
vlunerableIndividuals = totalPopulation - 1
infectedIndividuals = 1
recoveredIndividuals = 0
beta = 0.8  # infection rate
gamma = 0.1  # recovery rate


def differentialEquationSolver(sir, t):
    # sir[0] - S, sir[1] - I, sir[2] - R
    dsdt = - (beta * sir[0] * sir[1]) / totalPopulation
    didt = (beta * sir[0] * sir[1]) / totalPopulation - gamma * sir[1]
    drdt = gamma * sir[1]
    print(dsdt + didt + drdt)
    dsirdt = [dsdt, didt, drdt]
    return dsirdt


# initial conditions
sirInitial = (vlunerableIndividuals, infectedIndividuals, recoveredIndividuals)

# time points
timePoints = np.linspace(0, 100)

# solve ODE
# the parameters are, the equations, initial conditions,
# and time steps (between 0 and 100)
sir = odeint(differentialEquationSolver, sirInitial, timePoints)

plt.plot(timePoints, sir[:, 0], label='S(t)')
plt.plot(timePoints, sir[:, 1], label='I(t)')
plt.plot(timePoints, sir[:, 2], label='R(t)')

plt.legend("SIR model")

plt.xlabel('Time in number of days' ,fontsize=18)
plt.ylabel('Total Population' ,fontsize=18)
plt.title("SIR model",fontsize=18)
plt.grid()
plt.show()
