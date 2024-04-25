#!/bin/bash

echo "Before setting, GROUPS: $GROUPS"
unset GROUPS
echo "After unsetting, GROUPS: $GROUPS"

# Input size (N)
N=10000

# Ensure the executable permission is set
chmod +x number_crunching_likwid

# New variable name to avoid any conflicts
PERF_GROUPS=("FLOPS_DP" "L3" "CACHE" "DATA" "MEM")
echo "Reset PERF_GROUPS: ${PERF_GROUPS[@]}"

# Run the instrumented code with likwid-perfctr for each group
for GROUP in "${PERF_GROUPS[@]}"
do
    echo "Running group: $GROUP"
    likwid-perfctr -C 0 -g $GROUP -m ./number_crunching_likwid $N > "likwid_output/number_crunching_likwid_$GROUP.out"
done
