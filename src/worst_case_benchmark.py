import time
import sys
from sorting_algorithms import quicksort, counting_sort, merge_sort, quicksort_3_way
from benchmark_utils import get_clock_resolution # Assumendo che le utility siano qui

# Aumento del limite di ricorsione necessario per il caso peggiore di Quicksort O(n^2)
# Come indicato nel vostro codice originale
sys.setrecursionlimit(100000)

def generate_quicksort_worst_case(n):
    """
    Generates a descending array to trigger the O(n^2) worst case for 
    Quicksort with Lomuto partition.
    """
    return list(range(n, 0, -1))

def generate_mergesort_worst_case(n):
    """
    Generates an array using the 'perfect alternation' method to force 
    maximum comparisons in Merge Sort.
    """
    if n <= 1:
        return list(range(n))
    
    def perfect_alternation(size):
        if size == 1:
            return [0]
        left = perfect_alternation(size // 2)
        right = perfect_alternation(size - size // 2)
        # Interleave elements
        return [2 * x for x in left] + [2 * x + 1 for x in right]
    
    return perfect_alternation(n)

def generate_counting_worst_case(n, m_max):
    """
    Generates an array with a maximum range (m) to maximize 
    memory allocation overhead for Counting Sort.
    """
    # Array with unique elements spread across the maximum possible range
    import random
    return [random.randint(0, m_max) for _ in range(n)]

def run_worst_case_benchmark():
    """
    Measures performance under stress conditions as analyzed in Chapter 4.
    """
    print("Starting Worst-Case Analysis...")
    # Esempio per Quicksort O(n^2)
    for n in [1000, 5000, 10000]:
        arr = generate_quicksort_worst_case(n)
        start = time.perf_counter()
        quicksort(arr, 0, len(arr))
        end = time.perf_counter()
        print(f"Quicksort Worst Case (n={n}): {end-start:.5f}s")

if __name__ == "__main__":
    run_worst_case_benchmark()