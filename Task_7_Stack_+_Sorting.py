class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def to_list(self):
        return self.items

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Implementation
my_stack = Stack()
my_stack.push(88)
my_stack.push(14)
my_stack.push(42)
my_stack.push(7)

stack_list = my_stack.to_list()
print(f"Original List from Stack: {stack_list}")

sorted_stack_list = selection_sort(stack_list)
print(f"Sorted List: {sorted_stack_list}")