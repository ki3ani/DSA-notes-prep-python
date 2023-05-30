# We start by defining our Stack class. We'll use a Python list in this implementation.
class Stack:
    def __init__(self):
        # Initialize the stack with an empty list
        self.stack = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def push(self, data):
        # Add an element to the top of the stack
        self.stack.append(data)

    def pop(self):
        # Remove an element from the top of the stack
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        # View the top element of the stack without removing it
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.stack[-1]

# Now let's test our Stack class.

# We'll create a new Stack object
s = Stack()

# Test is_empty - returns True
print(s.is_empty()) 

# Test push
s.push(1)  
s.push(2)  
s.push(3)  

# Test is_empty again - returns False
print(s.is_empty()) 

# Test peek - returns 3
print(s.peek()) 

# Test pop - returns 3
print(s.pop()) 

# Test peek again - returns 2
print(s.peek()) 
