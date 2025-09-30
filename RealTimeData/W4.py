import matplotlib.pyplot as plt
import time

# N = 500
# water = [0] * N
# ink = [1] * 100
# u = 0
# D = 1
# t = 0
# dt = 0.1

# u_init = water
# u_init[200:300] = ink 
# u = u_init

# while True:
#     u_new = [0] * N
#     for i in range(N):
#         u_new[i] = u[i] + D*dt*(u[ (i + 1) % N]+ u[(i-1)%N] - 2*u[i])
#     u = u_new
#     t += 1
#     if t == 500:
#         break; 




data_size = (640,640)
@profile
def diffusion(u_in,u_out, dt, D=1.0):
    xmax, ymax = data_size

    for i in range(xmax):
        for j in range(ymax):
            dxx = (u_in[(i + 1) % xmax][j] +
                   u_in[(i - 1) % xmax][j] -
                   2.0 * u_in[i][j])
            
            dyy = (u_in[i][(j + 1) % ymax] +
                   u_in[i][(j - 1) % ymax] -
                   2.0 * u_in[i][j])
            
            u_out[i][j] = u_in[i][j] + D * dt * (dxx + dyy)
    
    return u_out

def dropInk(max_iter):
    xmax, ymax = data_size
    u = [[0.0] * ymax for _ in range(xmax)]
    u_new = [[0.0] * ymax for _ in range(xmax)]

    # Initialization
    ink_low = int(data_size[0] * 0.4)
    ink_high = int(data_size[0] * 0.6)
    
    for i in range(ink_low, ink_high):
        for j in range(ink_low, ink_high):
            u[i][j] = 0.005
            
    u_init = u

    start = time.time()
    for _ in range(max_iter):
        u = diffusion(u,u_new, 0.1)
        u, u_new = u_new, u
    end = time.time()

    return end - start, u_init, u


if __name__ == '__main__':

    run_time, u_init, u = dropInk(max_iter=100)
    # plt.figure(figsize=(5,5))
    # plt.imshow(u_init)
    # plt.axis("equal")
    # plt.savefig('diffusion_simulation.png')
    print(run_time)