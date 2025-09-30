import numpy as np
import time

data_size = (640,640)
def diffusion(u_in, dt, D=1.0):
    return u_in + dt*D*diffusion_op(u_in)

def diffusion_op(u_in):

    return (np.roll(u_in, +1, 0) + np.roll(u_in, -1, 0) + 
            np.roll(u_in, +1, 1) + np.roll(u_in, -1, 1) - 
            4 * u_in)
def dropInk(max_iter):
    xmax, ymax = data_size
    u = np.zeros(data_size)


    # Initialization
    ink_low = int(data_size[0] * 0.4)
    ink_high = int(data_size[0] * 0.6)
    
    u[ink_low:ink_high, ink_low:ink_high] = 0.005
    start = time.time()
    for i in range(max_iter):
        u = diffusion(u, 0.1)
    end = time.time()

    return end - start, u


if __name__ == '__main__':

    run_time,  u = dropInk(max_iter=100)
