"""
Given a queue of integers that are already sorted by absolute value, modify it such that integers are sorted normally. You
are allowed to use only one helper stack. For instance, the input queue at left should be converted to the one at right with
your function.
Example: {1, −3, 5, −8, 9, 12, −20} → {−20, −8, −3, 1, 5, 9, 12}

"""


from Queue import Queue
from Stack import Stack


def sorted_data(data):
    helper = Stack()
    sorting = Queue()
    positive = 0
    negative = 0
    i = 0
    length = len(data)
    while i < length:
        if data.front() < 0:
            helper.push(data.dequeue())
            negative += 1
        else:
            sorting.enqueue(data.dequeue())
            positive += 1
        i += 1

    k = 0
    while k < len(helper):
        sorting.enqueue(helper.pop())
        k += 1
    j = 0
    while j < positive:
        sorting.enqueue(sorting.dequeue())
        j += 1

    return sorting


parameter = Queue()
parameter.enqueue(1)
parameter.enqueue(-3)
parameter.enqueue(5)
parameter.enqueue(-8)
parameter.enqueue(9)
parameter.enqueue(12)
parameter.enqueue(-20)
print("Unsorted:")
print(parameter)

print("Sorted:")
print(sorted_data(parameter))
















