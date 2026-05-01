import math
def indexed_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal block size
    prev = 0

    # Finding the block where element is present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return False

    # Linear search for target in block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return False

    # If element is found
    if arr[prev] == target:
        return True
    return False

# Expected Output Setup
arr = [5, 10, 15, 20, 25, 30]
print(f"List: {arr}")
target = int(input("Enter element: "))

if indexed_search(arr, target):
    print("Element found")
else:
    print("Element not found")