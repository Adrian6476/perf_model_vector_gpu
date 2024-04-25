#include <algorithm>
#include <fstream>
#include <iostream>
#include <iomanip>
#include "tools.cuh"

__global__ void function_a_kernel(const double* A, const double* x, double* y, const int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        y[i] = 0;
        for (int j = 0; j < N; j++) {
            y[i] += A[i * N + j] * x[i];
        }
    }
}

__global__ void function_b_kernel(const double a, const double* u, const double* v, double* x, const int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        x[i] = a * u[i] + v[i];
    }
}

__global__ void function_c_kernel(const double s, const double* x, const double* y, double* z, const int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        if (i % 2 == 0) {
            z[i] = s * x[i] + y[i];
        } else {
            z[i] = x[i] + y[i];
        }
    }
}

__global__ void function_d_kernel(const double* u, const double* v, double* s, const int N) {
    __shared__ double shared_s;
    if (threadIdx.x == 0) {
        shared_s = 0;
    }
    __syncthreads();

    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        atomicAdd(&shared_s, u[i] * v[i]);
    }
    __syncthreads();

    if (threadIdx.x == 0) {
        atomicAdd(s, shared_s);
    }
}

void init_datastructures(double* u, double* v, double* A, const int N) {
    for (unsigned int i = 0; i < N; i++) {
        u[i] = static_cast<double>(i % 2);
        v[i] = static_cast<double>(i % 4);
    }
    for (unsigned int i = 0; i < N * N; i++) {
        A[i] = static_cast<double>(i % 8);
    }
}

void print_results_to_file(const double s, const double* x, const double* y,
                           const double* z, const double* A, const long long n,
                           std::ofstream& File) {
    unsigned int N = std::min(n, static_cast<long long>(30));

    File << "N: "
         << "\n"
         << n << "\n";
    File << "s: "
         << std::fixed
         << std::setprecision(1)
         << "\n"
         << s << "\n";
    File << "x: "
         << "\n";
    for (unsigned int i = 0; i < N; i++) {
        File << x[i] << " ";
    }
    File << "\n";
    File << "y: "
         << "\n";
    for (unsigned int i = 0; i < N; i++) {
        File << y[i] << " ";
    }
    File << "\n";
    File << "z: "
         << "\n";
    for (unsigned int i = 0; i < N; i++) {
        File << z[i] << " ";
    }
    File << "\n";
}

int main(int argc, char** argv) {
    long long N;
    if (argc == 2) {
        N = std::stoi(argv[1]);
    } else {
        std::cout << "Error: Missing problem size N. Please provide N as "
                     "commandline parameter. Usage example for N=10: "
                     "./number_crunching 10"
                  << std::endl;
        exit(0);
    }

    // Set up GPU
    setGPU();

    // Allocate memory on host
    double* u = new double[N];
    double* v = new double[N];
    double* A = new double[N * N];
    double* x = new double[N];
    double* y = new double[N];
    double* z = new double[N];

    // Initialize data on host
    init_datastructures(u, v, A, N);

    // Allocate memory on device
    double* d_u;
    double* d_v;
    double* d_A;
    double* d_x;
    double* d_y;
    double* d_z;
    double* d_s;
    ErrorCheck(cudaMalloc((void**)&d_u, N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_v, N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_A, N * N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_x, N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_y, N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_z, N * sizeof(double)), __FILE__, __LINE__);
    ErrorCheck(cudaMalloc((void**)&d_s, sizeof(double)), __FILE__, __LINE__);

    // Copy data from host to device
    ErrorCheck(cudaMemcpy(d_u, u, N * sizeof(double), cudaMemcpyHostToDevice), __FILE__, __LINE__);
    ErrorCheck(cudaMemcpy(d_v, v, N * sizeof(double), cudaMemcpyHostToDevice), __FILE__, __LINE__);
    ErrorCheck(cudaMemcpy(d_A, A, N * N * sizeof(double), cudaMemcpyHostToDevice), __FILE__, __LINE__);

    // Define grid and block dimensions
    dim3 blockSize(256);
    dim3 gridSize((N + blockSize.x - 1) / blockSize.x);

    // Launch kernels
    function_d_kernel<<<1, blockSize>>>(d_u, d_v, d_s, N);
    ErrorCheck(cudaGetLastError(), __FILE__, __LINE__);
    ErrorCheck(cudaDeviceSynchronize(), __FILE__, __LINE__);

    function_b_kernel<<<gridSize, blockSize>>>(2, d_u, d_v, d_x, N);
    ErrorCheck(cudaGetLastError(), __FILE__, __LINE__);
    ErrorCheck(cudaDeviceSynchronize(), __FILE__, __LINE__);

    function_a_kernel<<<gridSize, blockSize>>>(d_A, d_x, d_y, N);
    ErrorCheck(cudaGetLastError(), __FILE__, __LINE__);
    ErrorCheck(cudaDeviceSynchronize(), __FILE__, __LINE__);

    function_c_kernel<<<gridSize, blockSize>>>(0, d_x, d_y, d_z, N);
    ErrorCheck(cudaGetLastError(), __FILE__, __LINE__);
    ErrorCheck(cudaDeviceSynchronize(), __FILE__, __LINE__);

    // Copy results from device to host
    double s;
    ErrorCheck(cudaMemcpy(&s, d_s, sizeof(double), cudaMemcpyDeviceToHost), __FILE__, __LINE__);
    ErrorCheck(cudaMemcpy(x, d_x, N * sizeof(double), cudaMemcpyDeviceToHost), __FILE__, __LINE__);
    ErrorCheck(cudaMemcpy(y, d_y, N * sizeof(double), cudaMemcpyDeviceToHost), __FILE__, __LINE__);
    ErrorCheck(cudaMemcpy(z, d_z, N * sizeof(double), cudaMemcpyDeviceToHost), __FILE__, __LINE__);

    // Print results to file
    std::ofstream File("partial_results.out");
    print_results_to_file(s, x, y, z, A, N, File);

    std::cout << "For correctness checking, partial results have been written to "
                 "partial_results.out"
              << std::endl;

    // Free memory on device
    ErrorCheck(cudaFree(d_u), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_v), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_A), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_x), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_y), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_z), __FILE__, __LINE__);
    ErrorCheck(cudaFree(d_s), __FILE__, __LINE__);

    // Free memory on host
    delete[] u;
    delete[] v;
    delete[] A;
    delete[] x;
    delete[] y;
    delete[] z;

    return 0;
}
