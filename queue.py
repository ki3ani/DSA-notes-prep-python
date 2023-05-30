# Define the Queue class
class Queue:
    def __init__(self):
        """Initialize a new instance of the Queue class with an empty list."""
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty by checking the length of the list.
        Return True if the queue is empty, and False otherwise."""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue using the list's append method."""
        self.queue.append(item)

    def dequeue(self):
        """Remove an item from the front of the queue using the list's pop method.
        If the queue is empty, return a message saying "Queue is empty"."""
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)

    def size(self):
        """Return the number of items in the queue by checking the length of the list."""
        return len(self.queue)

    def peek(self):
        """Return the item at the front of the queue without removing it.
        If the queue is empty, return a message saying "Queue is empty"."""
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[0]

# Test the Queue class
q = Queue()  # Create a new Queue

print(q.is_empty())  # Test is_empty - should return True

# Test enqueue
q.enqueue("Apple")
q.enqueue("Banana")
q.enqueue("Cherry")

print(q.is_empty())  # Test is_empty again - should return False

print(q.peek())  # Test peek - should return "Apple"

print(q.dequeue())  # Test dequeue - should return "Apple"

print(q.peek())  # Test peek again - should return "Banana"
