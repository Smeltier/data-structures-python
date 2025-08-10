from typing import Any

class Stack:
    def __init__(self):
        self.items: list[Any] = []

    def __repr__(self) -> str:
        return f'Stack = {self.items}'

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Error, your Stack is empty.")
        return self.items.pop()
    
    def top(self) -> Any:
        if self.is_empty():
            raise IndexError("Error, your Stack is empty.")
        return self.items[-1]
    
    def clear(self) -> None:
        self.items.clear()
