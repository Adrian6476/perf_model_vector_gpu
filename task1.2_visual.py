import matplotlib.pyplot as plt

# Sample data
times = {
    10000: {'init_datastructures': 51.55, 'function_a': 48.76, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    20000: {'init_datastructures': 50.33, 'function_a': 49.97, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    30000: {'init_datastructures': 47.05, 'function_a': 53.25, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    40000: {'init_datastructures': 54.37, 'function_a': 45.93, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    50000: {'init_datastructures': 54.61, 'function_a': 45.69, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    60000: {'init_datastructures': 53.82, 'function_a': 46.48, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    70000: {'init_datastructures': 10.08, 'function_a': 90.22, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    80000: {'init_datastructures': 28.66, 'function_a': 71.65, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    90000: {'init_datastructures': 35.00, 'function_a': 65.30, 'std::operator&': 0.00, 'function_b': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00},
    100000: {'init_datastructures': 10.75, 'function_a': 89.53, 'function_b': 0.03, 'std::operator&': 0.00, 'function_c': 0.00, 'function_d': 0.00, 'print_results_to_file': 0.00}
}

# Prepare data for plotting
N_values = sorted(times.keys())
function_names = set()
for N, func_times in times.items():
    function_names.update(func_times.keys())

function_names = sorted(function_names)

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the execution times for each function
for function_name in function_names:
    y_values = [times[N].get(function_name, 0) for N in N_values]
    ax.plot(N_values, y_values, marker='o', label=function_name)

# Set labels and title
ax.set_xlabel('Input Size (N)')
ax.set_ylabel('Execution Time (%)')
ax.set_title('Execution Times for Different Functions')

# Add a legend
ax.legend()

# Show the plot
plt.show()
