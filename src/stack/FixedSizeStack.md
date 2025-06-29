# FixedSizeStack

## About

The `FixedSizeStack` class implements a stack (LIFO - Last In, First Out) with a fixed size. It allows for standard stack operations such as pushing and popping items, along with additional functionalities like checking if the stack is full or empty, clearing the stack, and searching for an item within the stack.

This class is ideal for situations where you want a stack with a predefined maximum capacity, ensuring the stack does not grow beyond a certain limit.

## Methods

### `__init__(self, max_length=1000)`
Initializes the stack with a maximum size of `max_length` and a pointer (`pointer`) that represents the top of the stack.

- **Parameters**:
  - `max_length` (int): The maximum size of the stack (optional, default is 1000).

### `push(self, item)`
Adds an item to the top of the stack. If the stack is full, it raises an `IndexError`.

- **Parameters**:
  - `item`: The item to be added to the stack.

- **Exceptions**:
  - Raises an `IndexError` exception if the stack is full.

### `is_full(self)`
Checks if the stack has reached its maximum size.

- **Return**:
  - `True` if the stack is full.
  - `False` otherwise.

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

### `size(self)`
Returns the number of elements currently in the stack.

- **Return**:
  - The number of items in the stack.

### `clear(self)`
Clears all items from the stack, resets the pointer to 0, and initializes the internal list with zeros.

### `contains(self, item)`
Checks if an item is present in the stack.

- **Parameters**:
  - `item`: The item to check.

- **Return**:
  - `True` if the item is present in the stack.
  - `False` otherwise.

## How to Import

You can import the `FixedSizeStack` class directly from the GitHub repository by installing it through `git` or using it in your project directly.

### Install via Git (Clone the Repository)

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/Smeltier/data-structures-python.git
   ```

2. Navigate to the `Stack` folder:
   ```bash
   cd data-structures-python/Stack
   ```

3. Import the `FixedSizeStack` class in your Python code:
   ```python
   from stack import FixedSizeStack

   stack = FixedSizeStack(5)
   stack.push(10)
   stack.push(20)
   stack.push(30)
   print(stack.top())  # Output: 30
   ```

### Directly Use in Your Project

Alternatively, you can download the `FixedSizeStack.py` file directly from the repository's `Stack` directory and import it into your project.

```python
from FixedSizeStack import FixedSizeStack

stack = FixedSizeStack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.top())  # Output: 30
```

## Example Usage

```python
# Importing the FixedSizeStack class
from stack import FixedSizeStack

# Creating an instance of the FixedSizeStack with a maximum size of 5
stack = FixedSizeStack(5)

# Adding elements
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
