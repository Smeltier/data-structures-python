class FixedSizeStack:
    def __init__(self, max_length = 1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0

    def push(self, item):
        if self.pointer >= self.max_length:
            raise IndexError("Stack Overflow")
        self.items[self.pointer] = item
        self.pointer += 1

    def is_full(self):
        return self.pointer >= self.max_length

    def is_empty(self):
        return self.pointer == 0

    def pop(self):
        if self.pointer == 0:
            raise IndexError("Error, your stack is empty")
        self.pointer -= 1
        return self.items[self.pointer]
    
    def top(self):
        if self.pointer == 0:
            raise IndexError("Error, your stack is empty")
        return self.items[self.pointer - 1]
    
    def size(self):
        return self.pointer
    
    def clear(self):
        self.pointer = 0
        self.items = [0] * self.max_length
    
    def contains(self, item):
        return item in self.items[:self.pointer]
