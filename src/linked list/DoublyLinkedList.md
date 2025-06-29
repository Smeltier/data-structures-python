# Doubly Linked List

## About

The `DoublyLinkedList` class implements a doubly linked list data structure, which allows for efficient insertion and removal of elements from both ends of the list. Each node in the list contains a reference to both the next node and the previous node, making traversal in both directions possible.

This class provides standard doubly linked list operations such as adding and removing elements from the front or back of the list, along with additional functionalities like checking the list size, checking if the list is empty, searching for an item, and reversing the list.

## Methods

### `__init__(self)`
Initializes an empty doubly linked list.

- **Parameters**:
  - None

### `get_size(self)`
Returns the number of elements currently in the list.

- **Return**:
  - The number of nodes in the list.

### `is_empty(self)`
Checks if the list is empty.

- **Return**:
  - `True` if the list is empty.
  - `False` otherwise.

### `add_front(self, value)`
Adds a node with the specified value to the front of the list.

- **Parameters**:
  - `value`: The value to be added to the front of the list.

### `add_back(self, value)`
Adds a node with the specified value to the back of the list.

- **Parameters**:
  - `value`: The value to be added to the back of the list.

### `remove_front(self)`
Removes and returns the value of the node at the front of the list. If the list is empty, it returns `None`.

- **Return**:
  - The value of the removed node.

### `remove_back(self)`
Removes and returns the value of the node at the back of the list. If the list is empty, it returns `None`.

- **Return**:
  - The value of the removed node.

### `front(self)`
Returns the value of the node at the front of the list. If the list is empty, it returns `None`.

- **Return**:
  - The value of the node at the front.

### `back(self)`
Returns the value of the node at the back of the list. If the list is empty, it returns `None`.

- **Return**:
  - The value of the node at the back.

### `search(self, value)`
Searches for a node containing the specified value in the list.

- **Parameters**:
  - `value`: The value to search for.

- **Return**:
  - `True` if the value is found in the list.
  - `False` otherwise.

### `reverse(self)`
Reverses the order of nodes in the list.

## How to Import

You can import the `DoublyLinkedList` class directly from the GitHub repository by installing it through `git` or using it in your project directly.

### Install via Git (Clone the Repository)

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Smeltier/data-structures-python.git
   ```

2. Navigate to the `DoublyLinkedList` folder:
   ```bash
   cd data-structures-python/DoublyLinkedList
   ```

3. Import the `DoublyLinkedList` class in your Python code:
   ```python
   from doubly_linked_list import DoublyLinkedList

   dll = DoublyLinkedList()
   dll.add_front(10)
   dll.add_back(20)
   dll.add_front(5)
   dll.add_back(30)
   print(dll.front())  # Output: 5
   dll.reverse()
   print(dll.front())  # Output: 30
   ```

### Directly Use in Your Project

Alternatively, you can download the `DoublyLinkedList.py` file directly from the repository's `DoublyLinkedList` directory and import it into your project.

```python
from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
dll.add_front(10)
dll.add_back(20)
dll.add_front(5)
dll.add_back(30)
print(dll.front())  # Output: 5
dll.reverse()
print(dll.front())  # Output: 30
```

## Example Usage

```python
# Importing the DoublyLinkedList class
from doubly_linked_list import DoublyLinkedList

# Creating an instance of the DoublyLinkedList class
dll = DoublyLinkedList()

# Adding elements to the list
dll.add_front(10)
dll.add_back(20)
dll.add_front(5)
dll.add_back(30)

# Checking the front item
print(dll.front())  # Output: 5

# Checking the back item
print(dll.back())   # Output: 30

# Removing the front item
dll.remove_front()

# Checking the size of the list
print(dll.get_size())  # Output: 3

# Searching for an item in the list
print(dll.search(20))  # Output: True

# Reversing the list
dll.reverse()
print(dll.front())  # Output: 30
```
