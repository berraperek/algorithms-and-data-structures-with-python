class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create(self, list1):
        """
        This function creates a circular linked list from a list.

        :param list1: It is a list to create circular linked list (CLL).
                      The first element is head of CLL and the last element of the list
                      is the tail of CLL.
        :return: None
        """
        for elem in list1:
            new_node = Node(elem)
            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head

    def printCLL(self):
        """
        Print the circular linked list (CLL) in the order starting from the first element.

        :return: None
        """
        if self.head is not None:
            temp = self.head
            while True:
                print(temp.value, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()
        else:
            print("The circular linked list is empty.")

    def getNext(self, n):
        """
        Get the value of the element which is the next element of the node
        whose value is n. If there is no such element in the list, the program
        should return -1.

        :param n: it is an integer
        :return: integer as explained above
        """
        temp = self.head
        if temp is not None:
            if n == temp.value:
                return temp.next.value
            while temp.next != self.head:
                temp = temp.next
                if temp.value == n:
                    return temp.next.value
            return
        else:
            return -1

    def getPrev(self, n):
        """
        Get the value of the element which is the previous element of the node
        whose value is n. If there is no such element in the list, the program
        should give the output -1.

        :param n: it is an integer
        :return: integer as explained above
        """
        temp = self.head
        if temp is not None:
            if n == temp.next.value:
                return temp.value
            while temp.next != self.head:
                temp = temp.next
                if temp.next.value == n:
                    return temp.value
            return
        else:
            return -1

    def insert(self, n):
        """
        Inserts an element with value n after the last element of the CLL.

        :param n: it is an integer
        :return: None
        """
        new_node = Node(n)
        if self.head is not None:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
        else:
            self.head = new_node
            new_node.next = self.head.next

    def delete(self, n):
        """
        Deletes all the elements with value n from CLL.

        :param n: it is an integer to be searched in CLL.
        :return: None
        """
        while self.head is not None and self.head.value == n:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head

        temp = self.head
        if temp is not None:
            while temp.next != self.head:
                if temp.next.value == n:
                    deleted_node = temp.next
                    temp.next = deleted_node.next
                else:
                    temp = temp.next

    def getContent(self, i):
        """
        Gets the value of the node with i th index in the CLL.

        :param i: it is an integer that indicates the index of element in the CLL.
        :return: the content (value) of the i th index element.
        """
        temp = self.head
        count = 0
        if temp is not None:
            while temp.next != self.head:
                if count == i:
                    return temp.value
                count += 1
                temp = temp.next

    def getIndex(self, n):
        """
        Gets the index of the last element whose value is n.

        :param n: it is an integer
        :return: the index of the last element whose value is n.
        """
        temp = self.head
        count = 0
        if temp is not None:
            while temp.next != self.head:
                if temp.value == n:
                    return count
                count += 1
                temp = temp.next

    def replace(self, n, m):
        """
        Replace the value of the elements (whose value is n) with m.

        :param n: it is an integer
        :param m: it is an integer
        :return: None
        """
        temp = self.head
        if temp is not None:
            if temp.value == n:
                temp.value = m
            while temp.next != self.head:
                if temp.next.value == n:
                    temp.next.value = m
                temp = temp.next


if __name__ == '__main__':
    cll = CircularLinkedList()
    cll.create([1, 2, 3, 4])
    cll.printCLL()
    nxt = cll.getNext(3)
    prv = cll.getPrev(3)
    cll.insert(5)
    cll.delete(3)
    val = cll.getContent(0)
    ind = cll.getIndex(4)
    cll.replace(4, 3)

