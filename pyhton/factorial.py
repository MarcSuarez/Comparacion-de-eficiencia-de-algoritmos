import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def facto_r(n):
    if n == 0 or n == 1:
        return 1
    return n * facto_r(n - 1)

def facto_i(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def benchmark(func, n, sample_interval=0.01):
    start = time.time()
    mem_samples = memory_usage((func, (n,)), interval=sample_interval)
    end = time.time()
    exec_time = end - start
    mem_usage = max(mem_samples)
    return exec_time, mem_usage

if __name__ == "__main__":
    # Valores de n para las pruebas
    n_values = [100,200,300,400,500,600,700,800,900]

    tiempos_r = []
    tiempos_i = []
    mem_r = []
    mem_i = []

    for n in n_values:
        # Recursivo (evitar n demasiado alto por límite de recursión)
        if n < 1000:
            t_r, m_r = benchmark(facto_r, n)
        else:
            t_r, m_r = None, None
        t_i, m_i = benchmark(facto_i, n)

        tiempos_r.append(t_r)
        mem_r.append(m_r)
        tiempos_i.append(t_i)
        mem_i.append(m_i)

    # ---- Gráfica de tiempo ----
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, tiempos_r, marker="o", label="Recursivo")
    plt.plot(n_values, tiempos_i, marker="o", label="Iterativo")
    plt.title("Tiempo de ejecución")
    plt.xlabel("n")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("time.png")
    plt.close()

    # ---- Gráfica de memoria ----
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, mem_r, marker="o", label="Recursivo")
    plt.plot(n_values, mem_i, marker="o", label="Iterativo")
    plt.title("Uso de memoria")
    plt.xlabel("n")
    plt.ylabel("Memoria (MiB)")
    plt.legend()
    plt.grid(True)
    plt.savefig("memory.png")
    plt.close()
