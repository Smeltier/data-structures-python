class Node:

    def __init__(self, value):
        
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
        self._size = 0
    
    def get_size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0

    def add_front(self, value):

        new_node = Node(value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node

        self._size += 1
        self.head = new_node

    def add_back(self, value):

        new_node = Node(value)
        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self._size += 1

    def remove_front(self) -> int:

        if not self.head:
            return None

        removed_value = self.head.value
        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self._size -= 1
        return removed_value

    def remove_back(self) -> int:

        if not self.tail:
            return None

        removed_value = self.tail.value
        self.tail = self.tail.prev

        if self.tail:
            self.tail.next = None
        else:
            self.head = None

        self._size -= 1    
        return removed_value
    
    def front(self) -> int:

        if self.head:
            return self.head.value
        else:
            return None
        
    def back(self) -> int:

        if self.tail:
            return self.tail.value
        else:
            return None
        
    
    def search(self, value) -> bool:
        current = self.head

        while current:
            if current.value == value:
                return True;
            current = current.next

        return False

    def reverse(self):
        current = self.head
        self.tail = self.head

        while current:
            current.next, current.prev = current.prev, current.next
            if not current.prev:
                self.head = current
            current = current.prev
