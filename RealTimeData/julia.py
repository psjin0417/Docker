
import time
from functools import wraps 
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


x1 = -1.8
x2 = 1.8
y1 = -1.8
y2 = 1.8

c_real = -0.62772
c_imag = -0.42193

# 2. decorator 
@timefn
@profile
def calculate_Julia_set(maxiter, zs, cs):

    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]

        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1

        output[i] = n
    return output

def build_julia_set(desired_width, max_iterations):

    x_step = (x2 - x1) / desired_width
    y_step = (y2 - y1) / desired_width

    x = []
    y = []

    ycoord = y2
    while ycoord >= y1:
        y.append(ycoord)
        ycoord -= y_step

    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    zs = []
    cs = []

    for ycoord in y:
        for xcoord in x:

            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    # 1. print 
    start_time = time.time()
    output = calculate_Julia_set(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_Julia_set.__name__ + " took", secs, "seconds")

    return output

desired_width = 1000
max_iterations = 300

julia_set_data = build_julia_set(desired_width, max_iterations)


# 3. timeit module
# python3 -m timeit -n 5 -r 1 -s "import julia1" "julia.build_julia_set(desired_width=1000, max_iterations=300)"

# 4. ubuntu time 
# time -p python3 julia.py
# time --verbose python3 julia.py

# 5. 