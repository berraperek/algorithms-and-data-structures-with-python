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


