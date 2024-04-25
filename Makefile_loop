# compiler
NVCC = nvcc
# Compiler flags
NVCCFLAGS = -O3 -arch=sm_86 -std=c++14

# target
TARGET = number_crunching_loop

# Build rules
all: $(TARGET)

$(TARGET): number_crunching_loop.cu
	$(NVCC) $(NVCCFLAGS) -o $(TARGET) number_crunching_loop.cu

# Clean rule
clean:
	rm -f $(TARGET)
