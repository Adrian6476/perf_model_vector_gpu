
#!/bin/bash
echo "Before setting, GROUPS: $GROUPS"
unset GROUPS
echo "After unsetting, GROUPS: $GROUPS"

# Input size (N)
N=10000

# Performance groups to measure
PERF_GROUPS=("FLOPS_DP" "L3" "CACHE" "DATA" "MEM")

# Run the instrumented code with likwid-perfctr for each group
for GROUP in "${PERF_GROUPS[@]}"
do
    likwid-perfctr -C 0 -g $GROUP -m ./number_crunching_likwid $N > "number_crunching_likwid_$GROUP.out"
done
