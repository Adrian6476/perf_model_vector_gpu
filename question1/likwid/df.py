import pandas as pd
import matplotlib.pyplot as plt

# Data for CACHE section
cache_data = {
    'Section': 'CACHE',
    'CPU Info': 'AMD EPYC 7702 64-Core Processor AMD K17 (Zen2) architecture 2.00 GHz',
    'Event': 'Region function_a, Group 1: CACHE',
    'RDTSC Runtime [s]': 0.344573,
    'call count': 1,
    'ACTUAL_CPU_CLOCK': 1144516000,
    'MAX_CPU_CLOCK': 688069700,
    'RETIRED_INSTRUCTIONS': 3200208000,
    'CPU_CLOCKS_UNHALTED': 1139759000,
    'DATA_CACHE_ACCESSES': 1702352000,
    'DATA_CACHE_REFILLS_ALL': 9308,
    'Runtime (RDTSC) [s]': 0.3446,
    'Runtime unhalted [s]': 0.5733,
    'Clock [MHz]': 3320.4667,
    'CPI': 0.3562,
    'data cache requests': 1702352000,
    'data cache request rate': 0.532,
    'data cache misses': 9308,
    'data cache miss rate': 2.908561e-06,
    'data cache miss ratio': 5.467729e-06
}

# Data for DATA section
data_data = {
    'Section': 'DATA',
    'CPU Info': 'AMD EPYC 7702 64-Core Processor AMD K17 (Zen2) architecture 2.00 GHz',
    'Event': 'Region function_a, Group 1: DATA',
    'RDTSC Runtime [s]': 0.343963,
    'call count': 1,
    'ACTUAL_CPU_CLOCK': 1144656000,
    'MAX_CPU_CLOCK': 686869100,
    'RETIRED_INSTRUCTIONS': 3200208000,
    'CPU_CLOCKS_UNHALTED': 1139987000,
    'LS_DISPATCH_LOADS': 1503063000,
    'LS_DISPATCH_STORES': 100220600,
    'Runtime (RDTSC) [s]': 0.3440,
    'Runtime unhalted [s]': 0.5734,
    'Clock [MHz]': 3326.6837,
    'CPI': 0.3562,
    'Load to store ratio': 14.9975
}

# Data for FLOPS_DP section
flops_dp_data = {
    'Section': 'FLOPS_DP',
    'CPU Info': 'AMD EPYC 7702 64-Core Processor AMD K17 (Zen2) architecture 2.00 GHz',
    'Event': 'Region function_a, Group 1: FLOPS_DP',
    'RDTSC Runtime [s]': 0.344367,
    'call count': 1,
    'ACTUAL_CPU_CLOCK': 1145961000,
    'MAX_CPU_CLOCK': 687661800,
    'RETIRED_INSTRUCTIONS': 3200208000,
    'CPU_CLOCKS_UNHALTED': 1141180000,
    'RETIRED_SSE_AVX_FLOPS_ALL': 200000000,
    'MERGE': 0,
    'Runtime (RDTSC) [s]': 0.3444,
    'Runtime unhalted [s]': 0.5741,
    'Clock [MHz]': 3326.6421,
    'CPI': 0.3566,
    'DP [MFLOP/s]': 580.7757
}

# Data for L3 section
l3_data = {
    'Section': 'L3',
    'CPU Info': 'AMD EPYC 7702 64-Core Processor AMD K17 (Zen2) architecture 2.00 GHz',
    'Event': 'Region function_a, Group 1: L3',
    'RDTSC Runtime [s]': 0.343499,
    'call count': 1,
    'ACTUAL_CPU_CLOCK': 1145341000,
    'MAX_CPU_CLOCK': 685933400,
    'RETIRED_INSTRUCTIONS': 3200208000,
    'CPU_CLOCKS_UNHALTED': 1139853000,
    'L3_ACCESS': 12802600,
    'L3_MISS': 12602170,
    'Runtime (RDTSC) [s]': 0.3435,
    'Runtime unhalted [s]': 0.5738,
    'Clock [MHz]': 3333.1933,
    'CPI': 0.3562,
    'L3 access bandwidth [MBytes/s]': 2385.3517,
    'L3 access data volume [GBytes]': 0.8194,
    'L3 access rate [%]': 0.4001,
    'L3 miss rate [%]': 0.3938,
    'L3 miss ratio [%]': 98.4345
}

# Data for MEM section
mem_data = {
    'Section': 'MEM',
    'CPU Info': 'AMD EPYC 7702 64-Core Processor AMD K17 (Zen2) architecture 2.00 GHz',
    'Event': 'Region function_a, Group 1: MEM',
    'RDTSC Runtime [s]': 0.344393,
    'call count': 1,
    'ACTUAL_CPU_CLOCK': 1143969000,
    'MAX_CPU_CLOCK': 687717400,
    'RETIRED_INSTRUCTIONS': 3200208000,
    'CPU_CLOCKS_UNHALTED': 1139623000,
    'DRAM_CHANNEL_0': 6608612,
    'DRAM_CHANNEL_1': 6610215,
    'Runtime (RDTSC) [s]': 0.3444,
    'Runtime unhalted [s]': 0.5731,
    'Clock [MHz]': 3320.5919,
    'CPI': 0.3561,
    'Memory bandwidth [MBytes/s]': 2456.5124,
    'Memory data volume [GBytes]': 0.8460
}

# Combine data from all sections
all_data = [cache_data, data_data, flops_dp_data, l3_data, mem_data]

# Create DataFrame
df = pd.DataFrame(all_data)


