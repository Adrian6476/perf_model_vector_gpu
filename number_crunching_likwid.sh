#!/bin/bash

# The performance counters or counter groups to measure
COUNTERS="FLOPS_DP:PMC0,FLOPS_AVX:PMC1,MEM_BW:PMC2,L3:PMC3"

# Input size (N)
N=10000

# Compile the instrumented code
g++ -DLIKWID_PERFMON -o number_crunching_likwid number_crunching_likwid.cpp -llikwid

# Run the instrumented code with likwid-perfctr
$likwid-perfctr -C 0 -g $COUNTERS -m ./number_crunching_likwid $N

# Save the output to a file
$likwid-perfctr -C 0 -g $COUNTERS -m ./number_crunching_likwid $N > number_crunching_likwid.out

# Clean up the executable
rm number_crunching_likwid
