<!-- Code from number_crunching.cpp -->
```cpp
#include <algorithm>
#include <fstream>
#include <iostream>
#include <iomanip>


double *function_a(const double *A, const double *x, const int N) {
  double *y = new double[N];
  for (unsigned int i = 0; i < N; i++) {
    y[i] = 0;
  }
  for (unsigned int i = 0; i < N; i++) {
    for (unsigned int j = 0; j < N; j++) {
      y[i] += A[i * N + j] * x[i];
    }
  }
  return y;
}

double *function_b(const double a, const double *u, const double *v, const int N) {
  double *x = new double[N];
  for (unsigned int i = 0; i < N; i++) {
    x[i] = a * u[i] + v[i];
  }
  return x;
}


double *function_c(const double s, const double *x, const double *y,
                   const int N) {
  double *z = new double[N];
  for (unsigned int i = 0; i < N; i++) {
    if (i % 2 == 0) {
      z[i] = s * x[i] + y[i];
    } else {
      z[i] = x[i] + y[i];
    }
  }
  return z;
}

double function_d(const double *u, const double *v, const int N) {
  double s = 0;
  for (unsigned int i = 0; i < N; i++) {
    s += u[i] * v[i];
  }
  return s;
}

void init_datastructures(double *u, double *v, double *A, const int N) {
  for (unsigned int i = 0; i < N; i++) {
    u[i] = static_cast<double>(i%2);
    v[i] = static_cast<double>(i%4);
  }

  for (unsigned int i = 0; i < N * N; i++) {
    A[i] = static_cast<double>(i%8);
  }
}

void print_results_to_file(const double s, const double *x, const double *y,
                           const double *z, const double *A, const long long n,
                           std::ofstream &File) {
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

int main(int argc, char **argv) {
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

  double *u = new double[N];
  double *v = new double[N];
  double *A = new double[N * N];

  init_datastructures(u, v, A, N);

  double s = function_d(u, v, N);
  double *x = function_b(2, u, v, N);
  double *y = function_a(A, x, N);
  double *z = function_c(s, x, y, N);

  std::ofstream File("partial_results.out");
  print_results_to_file(s, x, y, z, A, N, File);

  std::cout << "For correctness checking, partial results have been written to "
               "partial_results.out"
            << std::endl;

  delete[] u;
  delete[] v;
  delete[] A;
  delete[] x;
  delete[] y;
  delete[] z;

  EXIT_SUCCESS;
}
```
<!-- Code from Makefile -->
```make
CXX = g++
CXXFLAGS = -O3 -march=native

number_crunching: number_crunching.cpp
	     $(CXX) $(CXXFLAGS) -o number_crunching number_crunching.cpp

clean:
	rm number_crunching
```

<!-- Outputs from number_crunching_likwid -->
```
number_crunching_likwid_CACHE.out
--------------------------------------------------------------------------------
CPU name:    AMD EPYC 7702 64-Core Processor                
CPU type:    AMD K17 (Zen2) architecture
CPU clock:    2.00 GHz
--------------------------------------------------------------------------------
For correctness checking, partial results have been written to partial_results.out
--------------------------------------------------------------------------------
Region function_a, Group 1: CACHE
+-------------------+------------+
|    Region Info    | HWThread 0 |
+-------------------+------------+
| RDTSC Runtime [s] |   0.344573 |
|     call count    |          1 |
+-------------------+------------+

+------------------------+---------+------------+
|          Event         | Counter | HWThread 0 |
+------------------------+---------+------------+
|    ACTUAL_CPU_CLOCK    |  FIXC1  | 1144516000 |
|      MAX_CPU_CLOCK     |  FIXC2  |  688069700 |
|  RETIRED_INSTRUCTIONS  |   PMC0  | 3200208000 |
|   CPU_CLOCKS_UNHALTED  |   PMC1  | 1139759000 |
|   DATA_CACHE_ACCESSES  |   PMC2  | 1702352000 |
| DATA_CACHE_REFILLS_ALL |   PMC3  |       9308 |
+------------------------+---------+------------+

+-------------------------+--------------+
|          Metric         |  HWThread 0  |
+-------------------------+--------------+
|   Runtime (RDTSC) [s]   |       0.3446 |
|   Runtime unhalted [s]  |       0.5733 |
|       Clock [MHz]       |    3320.4667 |
|           CPI           |       0.3562 |
|   data cache requests   |   1702352000 |
| data cache request rate |       0.5320 |
|    data cache misses    |         9308 |
|   data cache miss rate  | 2.908561e-06 |
|  data cache miss ratio  | 5.467729e-06 |
+-------------------------+--------------+

```

```
number_crunching_likwid_DATA.out
--------------------------------------------------------------------------------
CPU name:    AMD EPYC 7702 64-Core Processor                
CPU type:    AMD K17 (Zen2) architecture
CPU clock:    2.00 GHz
--------------------------------------------------------------------------------
For correctness checking, partial results have been written to partial_results.out
--------------------------------------------------------------------------------
Region function_a, Group 1: DATA
+-------------------+------------+
|    Region Info    | HWThread 0 |
+-------------------+------------+
| RDTSC Runtime [s] |   0.343963 |
|     call count    |          1 |
+-------------------+------------+

+----------------------+---------+------------+
|         Event        | Counter | HWThread 0 |
+----------------------+---------+------------+
|   ACTUAL_CPU_CLOCK   |  FIXC1  | 1144656000 |
|     MAX_CPU_CLOCK    |  FIXC2  |  686869100 |
| RETIRED_INSTRUCTIONS |   PMC0  | 3200208000 |
|  CPU_CLOCKS_UNHALTED |   PMC1  | 1139987000 |
|   LS_DISPATCH_LOADS  |   PMC2  | 1503063000 |
|  LS_DISPATCH_STORES  |   PMC3  |  100220600 |
+----------------------+---------+------------+

+----------------------+------------+
|        Metric        | HWThread 0 |
+----------------------+------------+
|  Runtime (RDTSC) [s] |     0.3440 |
| Runtime unhalted [s] |     0.5734 |
|      Clock [MHz]     |  3326.6837 |
|          CPI         |     0.3562 |
|  Load to store ratio |    14.9975 |
+----------------------+------------+

```

```
number_crunching_likwid_FLOPS_DP.out
--------------------------------------------------------------------------------
CPU name:    AMD EPYC 7702 64-Core Processor                
CPU type:    AMD K17 (Zen2) architecture
CPU clock:    2.00 GHz
--------------------------------------------------------------------------------
For correctness checking, partial results have been written to partial_results.out
--------------------------------------------------------------------------------
Region function_a, Group 1: FLOPS_DP
+-------------------+------------+
|    Region Info    | HWThread 0 |
+-------------------+------------+
| RDTSC Runtime [s] |   0.344367 |
|     call count    |          1 |
+-------------------+------------+

+---------------------------+---------+------------+
|           Event           | Counter | HWThread 0 |
+---------------------------+---------+------------+
|      ACTUAL_CPU_CLOCK     |  FIXC1  | 1145961000 |
|       MAX_CPU_CLOCK       |  FIXC2  |  687661800 |
|    RETIRED_INSTRUCTIONS   |   PMC0  | 3200208000 |
|    CPU_CLOCKS_UNHALTED    |   PMC1  | 1141180000 |
| RETIRED_SSE_AVX_FLOPS_ALL |   PMC2  |  200000000 |
|           MERGE           |   PMC3  |          0 |
+---------------------------+---------+------------+

+----------------------+------------+
|        Metric        | HWThread 

0 |
+----------------------+------------+
|  Runtime (RDTSC) [s] |     0.3444 |
| Runtime unhalted [s] |     0.5741 |
|      Clock [MHz]     |  3326.6421 |
|          CPI         |     0.3566 |
|     DP [MFLOP/s]     |   580.7757 |
+----------------------+------------+

```

```
number_crunching_likwid_L3.out
--------------------------------------------------------------------------------
CPU name:    AMD EPYC 7702 64-Core Processor                
CPU type:    AMD K17 (Zen2) architecture
CPU clock:    2.00 GHz
--------------------------------------------------------------------------------
For correctness checking, partial results have been written to partial_results.out
--------------------------------------------------------------------------------
Region function_a, Group 1: L3
+-------------------+------------+
|    Region Info    | HWThread 0 |
+-------------------+------------+
| RDTSC Runtime [s] |   0.343499 |
|     call count    |          1 |
+-------------------+------------+

+----------------------+---------+------------+
|         Event        | Counter | HWThread 0 |
+----------------------+---------+------------+
|   ACTUAL_CPU_CLOCK   |  FIXC1  | 1145341000 |
|     MAX_CPU_CLOCK    |  FIXC2  |  685933400 |
| RETIRED_INSTRUCTIONS |   PMC0  | 3200208000 |
|  CPU_CLOCKS_UNHALTED |   PMC1  | 1139853000 |
|       L3_ACCESS      |  CPMC0  |   12802600 |
|        L3_MISS       |  CPMC1  |   12602170 |
+----------------------+---------+------------+

+--------------------------------+------------+
|             Metric             | HWThread 0 |
+--------------------------------+------------+
|       Runtime (RDTSC) [s]      |     0.3435 |
|      Runtime unhalted [s]      |     0.5738 |
|           Clock [MHz]          |  3333.1933 |
|               CPI              |     0.3562 |
| L3 access bandwidth [MBytes/s] |  2385.3517 |
| L3 access data volume [GBytes] |     0.8194 |
|       L3 access rate [%]       |     0.4001 |
|        L3 miss rate [%]        |     0.3938 |
|        L3 miss ratio [%]       |    98.4345 |
+--------------------------------+------------+

```

```
number_crunching_likwid_MEM.out
--------------------------------------------------------------------------------
CPU name:    AMD EPYC 7702 64-Core Processor                
CPU type:    AMD K17 (Zen2) architecture
CPU clock:    2.00 GHz
--------------------------------------------------------------------------------
For correctness checking, partial results have been written to partial_results.out
--------------------------------------------------------------------------------
Region function_a, Group 1: MEM
+-------------------+------------+
|    Region Info    | HWThread 0 |
+-------------------+------------+
| RDTSC Runtime [s] |   0.344393 |
|     call count    |          1 |
+-------------------+------------+

+----------------------+---------+------------+
|         Event        | Counter | HWThread 0 |
+----------------------+---------+------------+
|   ACTUAL_CPU_CLOCK   |  FIXC1  | 1143969000 |
|     MAX_CPU_CLOCK    |  FIXC2  |  687717400 |
| RETIRED_INSTRUCTIONS |   PMC0  | 3200208000 |
|  CPU_CLOCKS_UNHALTED |   PMC1  | 1139623000 |
|    DRAM_CHANNEL_0    |   DFC0  |    6608612 |
|    DRAM_CHANNEL_1    |   DFC1  |    6610215 |
+----------------------+---------+------------+

+-----------------------------+------------+
|            Metric           | HWThread 0 |
+-----------------------------+------------+
|     Runtime (RDTSC) [s]     |     0.3444 |
|     Runtime unhalted [s]    |     0.5731 |
|         Clock [MHz]         |  3320.5919 |
|             CPI             |     0.3561 |
| Memory bandwidth [MBytes/s] |  2456.5124 |
| Memory data volume [GBytes] |     0.8460 |
+-----------------------------+------------+
```

