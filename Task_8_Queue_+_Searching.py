class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        # Inserts element at the end of the list (typical queue behavior)
        self.items.append(item)
        
    def to_list(self):
        return self.items

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1 # Returning 1-based position
    return -1

# Implementation
my_queue = Queue()
my_queue.enqueue(100)
my_queue.enqueue(200)
my_queue.enqueue(300)
my_queue.enqueue(400)

queue_list = my_queue.to_list()
print(f"Queue List: {queue_list}")

target_val = 300
pos = linear_search(queue_list, target_val)

if pos != -1:
    print(f"Element {target_val} found at position {pos}")
else:
    print("Element not found")