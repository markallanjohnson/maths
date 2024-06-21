import numpy as np
import matplotlib.pyplot as plt

# Define the range for the parameter t
t = np.linspace(-3, 3, 400)  # Adjust the range and number of points as needed

# Define the parametric equations
x = 3*t + 2
y = 2*t + 3

# Calculate distances between consecutive points
dx = np.diff(x)
dy = np.diff(y)
distances = np.sqrt(dx**2 + dy**2)
cumulative_distance = np.cumsum(distances)
total_distance = cumulative_distance[-1]

# Define the interval for placing arrows (e.g., place arrows every 10% of the total curve length)
arrow_interval = total_distance / 10

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# Plot x(t)
axs[0].plot(t, x, label='x(t)')
axs[0].set_xlabel('t')
axs[0].set_ylabel('x')
axs[0].set_title('Plot of x(t)')
axs[0].legend()
axs[0].grid(True)
axs[0].axhline(0, color='black', linewidth=0.5)
axs[0].axvline(0, color='black', linewidth=0.5)

# Plot y(t)
axs[1].plot(t, y, label='y(t)')
axs[1].set_xlabel('t')
axs[1].set_ylabel('y')
axs[1].set_title('Plot of y(t)')
axs[1].legend()
axs[1].grid(True)
axs[1].axhline(0, color='black', linewidth=0.5)
axs[1].axvline(0, color='black', linewidth=0.5)

# Plot parametric curve (x, y)
axs[2].plot(x, y, label='Parametric curve (x, y)')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].set_title('Plot of Parametric Equations')
axs[2].legend()
axs[2].grid(True)
axs[2].axhline(0, color='black', linewidth=0.5)
axs[2].axvline(0, color='black', linewidth=0.5)

# Add arrows to show the direction of the curve in the parametric plot
for i in range(len(cumulative_distance)):
    if cumulative_distance[i] % arrow_interval < distances[i]:
        axs[2].arrow(x[i], y[i], dx[i], dy[i],
                     shape='full', lw=0, length_includes_head=True, head_width=0.1, head_length=0.1, color='red')

# Adjust layout
plt.tight_layout()
plt.show()
