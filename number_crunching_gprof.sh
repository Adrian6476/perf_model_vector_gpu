#!/bin/bash

# compile
g++ -pg -o number_crunching number_crunching.cpp

# run the program and collect data
echo "Performance analysis with gprof:" > number_crunching_gprof.out
for k in {1..10}
do
    N=$((k * 10000))
    echo "Running for N = $N" >> number_crunching_gprof.out
    ./number_crunching $N
    gprof number_crunching gmon.out | grep -A3 "time" >> number_crunching_gprof.out
done
