import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
    # Model parameters
    K = 121    # Number of times steps
    dt = 0.01  # Delta t
    c = 0.1    # Coefficient of drag
    g = -9.81  # Gravity
    # For constructing matrix B
    bx = 0
    by = 0
    bz = 0
    bvx = 0.25
    bvy = 0.25
    bvz = 0.1
    # For constructing matrix C
    rx = 1.0
    ry = 5.0
    rz = 5.0

    # Create 3D axes for plotting
    ax = Axes3D(plt.figure())

    #####################
    # Part 1:
    #
    # Load true trajectory and plot it
    # Normally, this data wouldn't be available in the real world
    #####################

    x_coords, y_coords, z_coords = np.loadtxt('P4_trajectory.txt',
                                              delimiter=',', usecols=(0,1,2),
                                              unpack=True)

    ax.plot(x_coords, y_coords, z_coords,
            '--b', label='True trajectory')

    #####################
    # Part 2:
    #
    # Read the observation array and plot it (Part 2)
    #####################

    arr = np.loadtxt('P4_measurements.txt', delimiter=',')

    C = np.diag(1./np.array([rx,ry,rz]))

    x_coords, y_coords, z_coords = [x.flatten() for x in np.hsplit(np.dot(arr,C), 3)]

    ax.plot(x_coords, y_coords, z_coords,
            '.g', label='Observed trajectory')

    #####################
    # Part 3:
    # Use the initial conditions and propagation matrix for prediction
    #####################

    A = np.identity(6) - np.diag([0,0,0,c*dt,c*dt,c*dt]) + np.diag([dt,dt,dt],k=3)
    a = np.array([0,0,0,0,0,g*dt])
    s = np.zeros(6*K).reshape(K,6)

    s[0] = np.array([0, 0, 2, 15, 3.5, 4.0])
    # Initial conditions for s0
    # Compute the rest of sk using Eq (1)
    for k in range(1,K):
        s[k] = np.dot(A,s[k-1]) + a

    x_coords, y_coords, z_coords = [x.flatten() for x in np.hsplit(s, 6)][:3]

    ax.plot(x_coords, y_coords, z_coords,
            '-k', label='Blind trajectory')

    #####################
    # Part 4:
    # Use the Kalman filter for prediction
    #####################

    # B = ?
    # C = ?

    # Initial conditions for s0 and Sigma0
    # Compute the rest of sk using Eqs (2), (3), (4), and (5)

    # ax.plot(x_coords, y_coords, z_coords,
    #         '-r', label='Filtered trajectory')

    # Show the plot
    ax.legend()
    plt.show()
