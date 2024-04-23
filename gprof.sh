#!/bin/bash

# Compile the code with profiling enabled
g++ -pg -O3 -march=native -o number_crunching number_crunching.cpp

# Run the code with different values of N and generate profiling data
for k in {1..10}; do
    N=$((k * 10000))
    echo "Running with N = $N"
    ./number_crunching $N
done

# Generate the profiling report
gprof ./number_crunching gmon.out > number_crunching_gprof.out
