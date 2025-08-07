import time
from memory_profiler import memory_usage, profile
import matplotlib as mpl

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

def facto_i(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def benchmark(func, n):
    start = time.time()
    mem = memory_usage((func, (n,)), max_iterations=1)
    end = time.time()
    print(f"{func.__name__}({n}) = {func(n)}")
    print(f"Tiempo: {end - start:.8f}s, Memoria: {max(mem):.2f} MiB\n")

if __name__ == "__main__":
    benchmark(facto_r, 100)
    benchmark(facto_i, 100)