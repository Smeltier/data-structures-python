# Stack

## About

The `Stack` class implements a stack (LIFO - Last In, First Out) data structure using a dynamic Python list. It allows for standard stack operations such as pushing and popping items, along with additional functionalities like checking the stack size, checking if the stack is empty, and clearing the stack.

This class is ideal for situations where you need a flexible stack without a predefined size limit.

## Methods

### `__init__(self)`
Initializes the stack with an empty list.

- **Parameters**:
  - None

### `push(self, item)`
Adds an item to the top of the stack.

- **Parameters**:
  - `item`: The item to be added to the stack.

### `size(self)`
Returns the number of elements currently in the stack.

- **Return**:
  - The number of items in the stack.

### `is_empty(self)`
Checks if the stack is empty.

- **Return**:
  - `True` if the stack is empty.
  - `False` otherwise.

### `pop(self)`
Removes and returns the item from the top of the stack. If the stack is empty, it raises an `IndexError`.

- **Return**:
  - The item removed from the top of the stack.

- **Exceptions**:
  - Raises an `IndexError` exception if the stack is empty.

### `top(self)`
Returns the item at the top of the stack without removing it. If the stack is empty, it raises an `IndexError`.

- **Return**:
  - The item at the top of the stack.

- **Exceptions**:
  - Raises an `IndexError` exception if the stack is empty.

### `clear(self)`
Clears all items from the stack, resetting it to an empty state.

### `contains(self, item)`
Checks if an item is present in the stack.

- **Parameters**:
  - `item`: The item to check.

- **Return**:
  - `True` if the item is present in the stack.
  - `False` otherwise.

## How to Import

You can import the `Stack` class directly from the GitHub repository by installing it through `git` or using it in your project directly.

### Install via Git (Clone the Repository)

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Smeltier/data-structures-python.git
   ```

2. Navigate to the `Stack` folder:
   ```bash
   cd data-structures-python/Stack
   ```

3. Import the `Stack` class in your Python code:
   ```python
   from stack import Stack

   stack = Stack()
   stack.push(10)
   stack.push(20)
   stack.push(30)
   print(stack.top())  # Output: 30
   ```

### Directly Use in Your Project

Alternatively, you can download the `Stack.py` file directly from the repository's `Stack` directory and import it into your project.

```python
from Stack import Stack

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.top())  # Output: 30
```

## Example Usage

```python
# Importing the Stack class
from stack import Stack

# Creating an instance of the Stack class
stack = Stack()

# Adding elements to the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Checking the top item
print(stack.top())  # Output: 30

# Removing the top item
stack.pop()

# Checking the size of the stack
print(stack.size())  # Output: 2

# Checking if an item is in the stack
print(stack.contains(10))  # Output: True

# Clearing the stack
stack.clear()
print(stack.is_empty())  # Output: True
```
