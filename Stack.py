"""
You need to implement your stack as a class with a member variable(a container type, i.e list) and member functions. You
will initialize the stack as:
myStack = Stack()
Your Stack class will have the following member functions:
 • init (): A function that initializes the stack object.
 • push(element): inserts a particular element into the stack.
 • pop(): removes element from the top of the stack and returns the element.
 • top(): returns the element that is at the top of the stack without removing the element.
 • isempty(): return whether the stack is empty or not. Returns True when the stack is empty, False otherwise.
 """

class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def isempty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def push(self, element):
        return self._data.append(element)

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        return self._data.pop()

    def top(self):
        if self.isempty():
            return "Stack is empty"
        return self._data[-1]


if __name__ == '__main__':
    myStack = Stack()


