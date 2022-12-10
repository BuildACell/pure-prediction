import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation
def dydt(y, t):
    return y

def solve_ode(input_number):
    """
    Solve the ODE with initial condition
    set to the input_number and display the plot
    """
    # Define the initial condition
    y0 = input_number

    # Define the time range for the solution
    t = np.linspace(0, 5, 100)

    # Solve the differential equation using odeint
    y = odeint(dydt, y0, t)

    fig, ax = plt.subplots()
    # Generate a plot of the solution
    ax.plot(t, y, 'b-')

    # Add labels and titles to the plot
    ax.set_xlabel('Time')
    ax.set_ylabel('y(t)')
    ax.set_title('Solution of the Differential Equation')
    return fig, ax