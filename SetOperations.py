from CircularLinkedList import CircularLinkedList


def union(cll1, cll2):
    """
    Finds the union of two circular linked lists, cll1 and cll2,
    and output the resultant CLL. The repeated elements will appear
    only once.

    :param cll1: The first circular linked list
    :param cll2: The second circular linked list
    :return: a new circular linked list which is union of two circular linked lists.
    """
    union_list = []
    temp1 = cll1.head
    if cll1.head is not None:
        while temp1.next != cll1.head:
            if temp1.value not in union_list:
                union_list.append(temp1.value)
            temp1 = temp1.next
        if temp1.value not in union_list:
            union_list.append(temp1.value)

    temp2 = cll2.head
    if cll2.head is not None:
        while temp2.next != cll2.head:
            if temp2.value not in union_list:
                union_list.append(temp2.value)
            temp2 = temp2.next
        if temp2.value not in union_list:
            union_list.append(temp2.value)

    resultant_CLL = CircularLinkedList()
    resultant_CLL.create(union_list)
    return resultant_CLL


def intersection(cll1, cll2):
    """
    Finds the intersection of two circular linked lists, cll1 and cll2,
    and output the resultant CLL. Only the common elements will appear
    in the intersecting CLL.

    :param cll1: The first circular linked list
    :param cll2: The second circular linked list
    :return: a new circular linked list which is intersection of two circular linked lists.
    """
    cll1_list = []
    temp1 = cll1.head
    if cll1.head is not None:
        while temp1.next != cll1.head:
            cll1_list.append(temp1.value)
            temp1 = temp1.next
        cll1_list.append(temp1.value)

    intersection_list = []
    temp2 = cll2.head
    if cll2.head is not None:
        while temp2.next != cll2.head:
            if temp2.value in cll1_list:
                intersection_list.append(temp2.value)
            temp2 = temp2.next
        if temp2.value in cll1_list:
            intersection_list.append(temp2.value)

    resultant_CLL = CircularLinkedList()
    resultant_CLL.create(intersection_list)
    return resultant_CLL


def difference(cll1, cll2):
    """
    Finds the difference of two circular linked lists, cll1 and cll2,
    and output the resultant CLL. Only the (cll1-cll2) elements will appear
    in the result CLL.

    :param cll1: The first circular linked list
    :param cll2: The second circular linked list
    :return: a new circular linked list which is difference of two circular linked lists.
    """
    difference_list = []
    temp1 = cll1.head
    if cll1.head is not None:
        while temp1.next != cll1.head:
            difference_list.append(temp1.value)
            temp1 = temp1.next
        difference_list.append(temp1.value)

    resultant_CLL = CircularLinkedList()
    resultant_CLL.create(difference_list)

    temp2 = cll2.head
    if cll2.head is not None:
        while temp2.next != cll2.head:
            if temp2.value in difference_list:
                resultant_CLL.delete(temp2.value)
            temp2 = temp2.next
        if temp2.value in difference_list:
            resultant_CLL.delete(temp2.value)

    return resultant_CLL


if __name__ == '__main__':
    cll1 = CircularLinkedList()
    cll1.create([0, 1, 2, 4, 8, 12])
    cll2 = CircularLinkedList()
    cll2.create([-1, 2, 3, 6, 9, 12])
    cll1.printCLL()
    cll2.printCLL()
    cll_U = union(cll1, cll2)
    cll_U.printCLL()
    cll_I = intersection(cll1, cll2)
    cll_I.printCLL()
    cll_D = difference(cll1, cll2)
    cll_D.printCLL()
