from typing import Optional

class FixedSizeStack:
    def __init__(self, max_length = 1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0

    def push(self, item):
        if self.pointer >= self.max_length:
            return
        self.items[self.pointer] = item
        self.pointer += 1

    def is_full(self) -> bool:
        return self.pointer >= self.max_length

    def is_empty(self) -> bool:
        return self.pointer == 0

    def pop(self) -> Optional[int]:
        if self.pointer == 0:
            return None
        self.pointer -= 1
        return self.items[self.pointer]
    
    def top(self) -> Optional[int]:
        if self.pointer == 0:
            return None
        return self.items[self.pointer - 1]
    
    def size(self) -> int:
        return self.pointer
    
    def clear(self):
        self.pointer = 0
    
    def contains(self, item) -> bool:
        return item in self.items[:self.pointer]
