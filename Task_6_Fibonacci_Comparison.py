import time

def fibonacci_iterative(n):
    if n <= 0: return 0
    elif n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Global variable to count recursive calls
recursive_calls_count = 0 

def fibonacci_recursive(n):
    global recursive_calls_count
    recursive_calls_count += 1
    if n <= 0: return 0
    elif n == 1: return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter position for Fibonacci: "))

# Measure Iterative
start_time = time.time()
iter_result = fibonacci_iterative(n)
iter_time = time.time() - start_time

# Measure Recursive
recursive_calls_count = 0
start_time = time.time()
rec_result = fibonacci_recursive(n)
rec_time = time.time() - start_time

print(f"\nIterative Result: {iter_result} (Time: {iter_time:.6f} sec)")
print(f"Recursive Result: {rec_result} (Time: {rec_time:.6f} sec)")
print(f"Total recursive calls made: {recursive_calls_count}")
print("\nEfficiency Comparison: Iterative approach is faster and uses O(1) space, while the recursive approach without memoization has an exponential time complexity O(2^n) causing high redundant calculations.")