#!/bin/bash

# The number of threads
export OMP_NUM_THREADS=1

# Run the instrumented code with likwid-perfctr
likwid-perfctr -C 0 -g FLOPS_DP -m ./number_crunching_likwid 10000 > number_crunching_likwid.out
