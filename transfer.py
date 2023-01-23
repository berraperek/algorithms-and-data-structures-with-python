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



