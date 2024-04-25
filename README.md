# Performance Modelling, Vectorisation, and GPU Programming Coursework

This repository contains the coursework for the Performance Modelling, Vectorisation, and GPU Programming module (COMP 52315). The coursework focuses on analysing and optimising the performance of a given C++ code named `number_crunching.cpp`.

## Project Structure

The project is organised into the following directories:

- `question1/`: Contains files related to Question 1 of the coursework.
  - `gprof/`: Contains files for profiling the code using gprof.
  - `likwid/`: Contains files for profiling the code using likwid and generating the roofline model.
- `question2/`: Contains files related to Question 2 of the coursework.
  - `number_crunching_loop/`: Contains files for the GPU implementation with loop parallelism.
  - `number_crunching_task/`: Contains files for the GPU implementation with task parallelism.
- `plots/`: Contains generated plots and visualisations.

## Requirements

To run the code and reproduce the results, the following dependencies are required:

- C++ compiler (e.g., g++)
- CUDA Toolkit
- likwid profiling tool
- Python 3 with the following libraries:
  - Matplotlib
  - NumPy
  - Pandas
- Graphviz (for generating the task graph visualisation)

## Usage

### Question 1

1. Navigate to the `question1/gprof/` directory and run the `number_crunching_gprof.sh` script to profile the code using gprof.
2. Navigate to the `question1/likwid/` directory and run the `number_crunching_likwid.sh` script to profile the code using likwid.
3. Run the `df.py` script to generate the roofline model plot.

### Question 2

1. Navigate to the `question2/number_crunching_loop/` directory and run `make` to compile the GPU implementation with loop parallelism.
2. Run the `number_crunching_loop` executable with the desired input size as a command-line argument.
3. Navigate to the `question2/number_crunching_task/` directory and run `make` to compile the GPU implementation with task parallelism.
4. Run the `number_crunching_task` executable with the desired input size as a command-line argument.
5. To generate the task graph visualisation:
   - Install Graphviz on your system.
   - Run `dot -Tpng task_graph.dot -o task_graph.png` to generate the task graph image.

## Results

The `plots/` directory contains the generated plots and visualisations, including:

- `Task 1.2: Function Execution Time vs Input Size (N).png`: Plot showing the execution time of different functions with varying input sizes.
- `Roofline Model.png`: Roofline model plot generated from the likwid profiling results.
- `task_graph.png`: Task graph visualisation generated using Graphviz.

The `partial_results.out` files in the `question2/` subdirectories contain the partial results of the GPU implementations for correctness checking.

## Report

The detailed analysis, methodology, and findings of the coursework are documented in the `report_dgwz78.pdf` file.