"""
Sorting Algorithms Implementation
Part of the Empirical Analysis Project (2025).
Includes: Quicksort, Counting Sort, Quicksort 3-way, and Merge Sort.
"""

def quicksort(arr, low, high):
    """
    Standard Quicksort implementation using Lomuto partition.
    Time Complexity: Average O(n log n), Worst O(n^2)[cite: 165].
    Space Complexity: O(log n) due to recursion stack.
    """
    if high - low <= 1:
        return

    pivot_index = _partition(arr, low, high)
    quicksort(arr, low, pivot_index - 1)
    quicksort(arr, pivot_index, high)

def _partition(arr, low, high):
    """Helper function for quicksort to handle partitioning."""
    k = l = low
    pivot = arr[high - 1]

    while l < high:
        if arr[l] <= pivot:
            arr[k], arr[l] = arr[l], arr[k]
            k += 1
        l += 1
    return k

def counting_sort(arr):
    """
    Counting Sort implementation.
    Efficient for small ranges (m) of integers[cite: 86, 129].
    Time Complexity: O(n + k) where k is the range of input[cite: 83].
    Space Complexity: O(n + k).
    """
    if not arr:
        return arr

    min_val, max_val = _search_min_max(arr)
    range_val = max_val - min_val + 1
    
    # Frequency array
    count = [0] * range_val
    output = [0] * len(arr)

    for x in arr:
        count[x - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build output array (stable sorting)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output

def _search_min_max(arr):
    """Finds the minimum and maximum values in an array."""
    min_v = max_v = arr[0]
    for x in arr:
        if x < min_v: min_v = x
        elif x > max_v: max_v = x
    return min_v, max_v

def quicksort_3_way(arr, low, high):
    """
    Quicksort 3-way (Dutch National Flag) implementation.
    Optimized for arrays with many duplicate elements[cite: 128].
    Time Complexity: O(n log n) average, O(n) if all keys are equal.
    """
    if low < high:
        lt, gt = _partition_3_way(arr, low, high)
        quicksort_3_way(arr, low, lt - 1)
        quicksort_3_way(arr, gt, high)

def _partition_3_way(arr, low, high):
    """Partitioning logic for 3-way quicksort."""
    pivot = arr[low]
    lt, gt, i = low, low, low
    while i <= high:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            gt += 1
            i += 1
        elif arr[i] > pivot:
            i += 1
        else:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt += 1
            i += 1
    return lt, gt

def merge_sort(arr):
    """
    Merge Sort implementation.
    Stable sort that maintains O(n log n) in all cases[cite: 33, 188].
    Not affected by initial data distribution[cite: 135, 190].
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)

def _merge(left, right):
    """Merges two sorted sub-arrays."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result