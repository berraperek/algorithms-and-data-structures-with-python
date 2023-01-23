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

