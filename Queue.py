"""
You need to implement your queue as a class with a member variable(a container type, i.e list) and member functions. You
will initialize the queue as:
myQueue = Queue() 
Your Queue class will have the following member functions:
 • init (): A function that initializes the queue object.
 • enqueue(element): inserts a particular element into the stack.
 • dequeue(): removes element from the front of the queue and returns the element.
 • front(): returns the element that is at the front of the queue without removing the element.
 • isempty(): return whether the queue is empty or not. Returns True when the queue is empty, False otherwise.
 
 """

class Queue:
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

    def enqueue(self, element):
        return self._data.append(element)

    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        return self._data.pop(0)

    def front(self):
        if self.isempty():
            return "Queue is empty"
        return self._data[0]


if __name__ == '__main__':
    myQueue = Queue()

