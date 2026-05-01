def linear_search(arr, target):
    # Iterates through the list
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1  # Returning position (1-based index)
    return -1

# Expected Output Setup
arr = [10, 20, 30, 40, 50]
print(f"List: {arr}")
target = int(input("Enter element to search: "))

position = linear_search(arr, target)

if position != -1:
    print(f"Element found at position {position}")
else:
    print("Element not found")