from typing import Any

class FixedSizeStack:
    def __init__(self, max_length = 1000):
        self.items:      list[Any] = [0] * max_length
        self.max_length: int       = max_length
        self.pointer:    int       = 0

    def push(self, item: Any) -> None:
        if self.pointer >= self.max_length:
            return
        self.items[self.pointer] = item
        self.pointer += 1

    def is_full(self) -> bool:
        return self.pointer >= self.max_length

    def is_empty(self) -> bool:
        return self.pointer == 0

    def pop(self) -> Any:
        if self.pointer == 0:
            return None
        self.pointer -= 1
        return self.items[self.pointer]
    
    def top(self) -> Any:
        if self.pointer == 0:
            return None
        return self.items[self.pointer - 1]
    
    def size(self) -> int:
        return self.pointer
    
    def clear(self) -> None:
        self.pointer = 0
    
    def contains(self, item) -> bool:
        return item in self.items[:self.pointer]
