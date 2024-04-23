import matplotlib.pyplot as plt
import matplotlib as mpl

# Data from the table
N = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
init_datastructures_time = [0.37, 1.40, 2.74, 6.59, 10.38, 14.55, 1.92, 8.81, 15.16, 4.13]
function_a_time = [0.35, 1.39, 3.10, 5.57, 8.69, 12.57, 17.14, 22.02, 28.28, 34.40]
function_b_time = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01]
function_c_time = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
function_d_time = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

# Activate ggplot style
plt.style.use('ggplot')

# Setting the font to 'Liberation Sans', which is similar to Arial
mpl.rcParams['font.family'] = 'Liberation Sans'
mpl.rcParams['font.size'] = 10 

# Create figure and plot area
fig, ax = plt.subplots(figsize=(6, 4), dpi=300)  # Adjust size as per journal's requirements

# Plot data with ggplot style
ax.plot(N, init_datastructures_time, marker='o', linestyle='-', label='init_datastructures')
ax.plot(N, function_a_time, marker='v', linestyle='--', label='function_a')
ax.plot(N, function_b_time, marker='^', linestyle='-.', label='function_b', alpha=0.7)
ax.plot(N, function_c_time, marker='s', linestyle=':', label='function_c', alpha=0.5)
ax.plot(N, function_d_time, marker='*', linestyle='-', label='function_d', alpha=0.3)


# Label axes and add a title
ax.set_xlabel('Input Size (N)', fontsize=12)
ax.set_ylabel('Execution Time (s)', fontsize=12)
ax.set_title('Task 1.2: Function Execution Time vs Input Size (N)', fontsize=16)

# Improve the legend
ax.legend(frameon=True, loc='best', fontsize=10)

# Export as vector graphic for best quality
plt.savefig('plots/Task 1.2: Function Execution Time vs Input Size (N).png')

# Show plot
plt.show()
