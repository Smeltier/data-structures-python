class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Error, your Stack is empty.")
        return self.items.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError("Error, your Stack is empty.")
        return self.items[-1]
    
    def clear(self):
        self.items = []
