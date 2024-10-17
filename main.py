import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------
# Heat Equation Simulation using Explicit Method
# --------------------------------------------

# Physical parameters
L = 1.0            # Length of the rod (meters)
T = 0.5            # Total time to simulate (seconds)
alpha = 1e-4       # Thermal diffusivity (m^2/s)

# Numerical parameters
nx = 51            # Number of spatial grid points
nt = 5000          # Number of time steps
dx = L / (nx - 1)  # Spatial step size
dt = T / nt        # Time step size

# Stability condition for explicit method in 1D:
# alpha * dt / dx^2 <= 0.5
# Check if the chosen dt satisfies the stability condition
stability_condition = alpha * dt / dx**2
if stability_condition > 0.5:
    raise ValueError("Stability condition violated: alpha*dt/dx^2 should <= 0.5")
else:
    print(f"Stability condition satisfied: alpha*dt/dx^2 = {stability_condition}")

# Create spatial grid
x = np.linspace(0, L, nx)

# Initialize temperature distribution
# For example, initial temperature is 100 at the center and 0 elsewhere
u_initial = np.zeros(nx)
u_initial[int(nx/2)] = 100.0  # Initial heat at the center

# Initialize temperature array
u = u_initial.copy()

# To store temperature profiles at different times for visualization
u_profiles = [u_initial.copy()]
times = [0.0]

# Time-stepping loop
for n in range(1, nt+1):
    # Create a copy of the current temperature distribution
    u_new = u.copy()
    
    # Update temperature for each interior point
    for i in range(1, nx-1):
        # Explicit finite difference formula for heat equation
        u_new[i] = u[i] + alpha * dt / dx**2 * (u[i+1] - 2*u[i] + u[i-1])
    
    # Update temperature array
    u = u_new.copy()
    
    # Save profiles at specific time intervals for visualization
    if n % (nt // 10) == 0:
        u_profiles.append(u.copy())
        times.append(n * dt)
        print(f"Time step {n}, Time {n*dt:.4f} s")

# Plotting the results
plt.figure(figsize=(8,6))
for idx, profile in enumerate(u_profiles):
    plt.plot(x, profile, label=f't={times[idx]:.3f} s')

plt.title('Heat Equation Simulation using Explicit Method')
plt.xlabel('Position along the rod (m)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()