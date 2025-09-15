import numpy as np
import time

# Define the coordinates for the Julia set grid
x1 = -1.8
x2 = 1.8
y1 = -1.8
y2 = 1.8

# Define the constant 'c' for the Julia set calculation
c_real = -0.62772
c_imag = -0.42193

def calculate_Julia_set_np(maxiter, zs, c_val):
    """
    Calculate output array using Julia update rule with NumPy.
    This version is optimized for vectorized operations.
    """
    # Create an output array filled with maxiter
    output = np.full(zs.shape, maxiter, dtype=np.int32)
    # Get a boolean mask for points that are still active (not yet escaped)
    active = np.full(zs.shape, True)

    for n in range(maxiter):
        # Update z only for active points
        z_active = zs[active]
        zs[active] = z_active * z_active + c_val

        # Check for escape condition (abs(z) > 2)
        escaped_mask = (np.abs(zs) > 2) & active
        
        # Update output for newly escaped points and deactivate them
        output[escaped_mask] = n
        active[escaped_mask] = False
        
        # If all points have escaped, break the loop
        if not np.any(active):
            break
            
    return output

def build_julia_set_np(desired_width, max_iterations):
    """
    Create a 2D grid of complex numbers and calculate the Julia Set using NumPy.
    """
    # Use np.linspace to generate coordinates efficiently
    # The number of y-coordinates should be proportional to the x-coordinates to maintain aspect ratio
    desired_height = int(desired_width * (y2 - y1) / (x2 - x1))
    
    x = np.linspace(x1, x2, desired_width)
    y = np.linspace(y2, y1, desired_height)

    # Create a 2D grid of complex numbers
    xv, yv = np.meshgrid(x, y)
    zs = xv + 1j * yv
    
    # Use a single complex constant
    c_val = complex(c_real, c_imag)

    print(f"Grid size: {desired_width}x{desired_height} = {desired_width * desired_height} points.")
    
    # Call the calculate_Julia_set function with the generated grid
    start_time = time.time()
    output = calculate_Julia_set_np(max_iterations, zs.ravel(), c_val)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_Julia_set_np.__name__ + " took", secs, "seconds")
    
    # Reshape the 1D output array back to 2D
    return output.reshape(desired_height, desired_width)

# Example usage with a larger width
desired_width = 1000  # Try a larger value like 500
max_iterations = 300

# Call the function to generate the Julia set data
julia_set_data = build_julia_set_np(desired_width, max_iterations)

# To visualize the data, you can use matplotlib.pyplot as an image.
# For example:
try:
    import matplotlib.pyplot as plt
    plt.imshow(julia_set_data, cmap='viridis', extent=[x1, x2, y1, y2])
    plt.colorbar(label='Iterations to diverge')
    plt.title('Julia Set')
    plt.show()
except ImportError:
    print("Matplotlib not installed. Please install it to visualize the output: pip install matplotlib")