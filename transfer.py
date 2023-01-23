"""
Implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so that the element
that starts at the top of S is the first to be inserted onto T, and the element at the bottom of S ends up at the top of T.

"""

from Stack import Stack

S = Stack()
T = Stack()


def transfer(S, T):
    if S.isempty():
        return "S is empty."
    else:
        for i in range(len(S)):
            T.push(S.pop())
        return T



