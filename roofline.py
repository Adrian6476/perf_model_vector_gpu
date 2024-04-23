import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl  # Make sure this import is included

# Activate ggplot style
plt.style.use('ggplot')

# Setting the font to 'Liberation Sans', which is similar to Arial
mpl.rcParams['font.family'] = 'Liberation Sans'
mpl.rcParams['font.size'] = 10 

# Peak performance and memory bandwidth (adjust according to your system)
peak_performance = 1000  # GFLOP/s (convert to MFLOP/s to match observed_performance)
peak_memory_bandwidth = 200  # GB/s

# Operational intensity and observed performance of the hotspot function
operational_intensity = 0.1  # FLOP/byte (calculated from Task 1.1)
observed_performance = 580.7757  # MFLOP/s (obtained from likwid profiling)

# Create a log-log scale plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the roofline
oi_values = np.array([0.01, 100])  # Range of operational intensity values for the roofline
ax.loglog(oi_values, [peak_performance * 1000] * len(oi_values), label='Peak Performance (GFLOP/s)', linestyle='--')  # Convert to MFLOP/s
ax.loglog(oi_values, oi_values * peak_memory_bandwidth * 1000, label='Memory Bandwidth (MFLOP/s)')  # Convert GB/s to MFLOP/s scaling by 1000

# Plot the hotspot function
ax.loglog(operational_intensity, observed_performance, 'ro', label='Hotspot Function')

ax.set_xlabel('Operational Intensity (FLOP/byte)')
ax.set_ylabel('Performance (MFLOP/s)')
ax.set_title('Roofline Model')
ax.legend()
ax.grid(True)  # Enhanced grid visibility
plt.savefig('plots/Roofline Model')
plt.show()
