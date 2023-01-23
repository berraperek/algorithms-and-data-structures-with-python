"""
Write a program that finds prime numbers using the Sieve of Erastosthenes, an algorithm devised by a Greek
mathematician of the same name who lived in the third century BC. The algorithm finds all prime numbers up to some
maximum value n.

"""

from Queue import Queue


def sieve_of_eratosthenes(n):
    numbers = Queue()

    for i in range(2, n + 1):
        numbers.enqueue(i)

    result = Queue()

    while True:
        value = numbers.dequeue()
        result.enqueue(value)
        queue_length = len(numbers)
        i = 0
        while i < queue_length:
            next_number = numbers.dequeue()
            if next_number % value != 0:
                numbers.enqueue(next_number)
            i += 1
        if value > (n ** (1 / 2)):
            break

    remaining_length = len(numbers)
    i = 0
    while i < remaining_length:
        result.enqueue(numbers.dequeue())
        i += 1

    return result


