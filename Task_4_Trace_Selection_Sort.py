def trace_selection_sort(arr):
    n = len(arr)
    # We only need n-1 passes 
    for i in range(n - 1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        # Displaying the list after each pass
        print(f"Pass {i+1}:")
        print(arr)

# Expected Output Setup
arr = [64, 25, 12, 22, 11]
trace_selection_sort(arr)