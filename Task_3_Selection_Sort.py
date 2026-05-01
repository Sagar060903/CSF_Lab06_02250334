def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find the minimum element in remaining unsorted array
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Expected Output Setup
original_list = [64, 25, 12, 22, 11]
print(f"Original List: {original_list}")

# Using .copy() to avoid modifying the original list for display purposes
sorted_list = selection_sort(original_list.copy())
print(f"Sorted List: {sorted_list}")