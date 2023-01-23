"""
Problem:

A government agency asks a software company to make a tender management system. This system includes the following
features of a binary search tree (BST) based software.
1. The tender management system based on BST is implemented.
2. While each company joins the tender, they enter the company name and the bid price into the tender application
   system.
3. The first joining company for the tender is considered the root of BST. A function (joinTender) must fulfill this
   service.
4. Subsequently, the system places the joining companies in the BST according to their bid price. (joinTender) function
   must fulfill this service.
5. In case a company wants to withdraw from tender, a function (withdrawFromTender) must complete this service.
6. A function called findWinner finds the minimum bid price and returns the company name and its bid price.
7. The software must have a function (printMaxtoMin) that prints the joining companies according to their bid prices
   (from maximum to minimum bid price).
8. The software must have a function (printInOrder) that prints the joining companies in in-order according to the
   formed BST.
9. The software must have a function (printPreOrder) that prints the joining companies in pre-order according to the
   formed BST.
10. The software must have a function (printPostOrder) that prints the joining companies in post-order according to
    the formed BST.

"""

class Company:
    def __init__(self, name, bidPrice):
        self.name = name
        self.bidPrice = bidPrice
        self.left = None
        self.right = None

    def searchSameBidPrice(self, bidPrice):
        """
        This function checks whether there is a company with the same bid price.
        :param bidPrice: (int): The bid price the company offers.
        :return: boolean value if bidPrice is found in the tree
        """
        if bidPrice == self.bidPrice:
            return True
        if bidPrice < self.bidPrice:
            if self.left == None:
                return False
            return self.left.searchSameBidPrice(bidPrice)
        if self.right == None:
            return False
        return self.right.searchSameBidPrice(bidPrice)


    def joinTender(self, name, bidPrice):
        """
        This function adds a new company to the tree.
        :param name: string: name of the company
        :param bidPrice: int: bid price of the company
        :return: None
        """
        if not self.bidPrice:
            self.bidPrice = bidPrice
            return
        if self.bidPrice == bidPrice:
            return
        if bidPrice < self.bidPrice:
            if self.left:
                self.left.joinTender(name, bidPrice)
                return
            self.left = Company(name, bidPrice)
            return
        if bidPrice > self.bidPrice:
            if self.right:
                self.right.joinTender(name, bidPrice)
                return
            self.right = Company(name, bidPrice)


    def withdrawfromTender(self, bidPrice):
        """
        This function finds the company according to its bid price and removes it from the tree.
        :param bidPrice: int: bid price of the company
        :return: None
        """
        if self == None:
            return self
        if bidPrice < self.bidPrice:
            if self.left:
                self.left = self.left.withdrawfromTender(bidPrice)
            return self
        if bidPrice > self.bidPrice:
            if self.right:
                self.right = self.right.withdrawfromTender(bidPrice)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.bidPrice = min_larger_node.bidPrice
        self.right = self.right.withdrawfromTender(min_larger_node.bidPrice)
        return self


    def findWinner(self):
        """
        This function finds the company with the lowest bid price.
        :return: tuple: the name and the bid price of the winning company
        """
        current = self
        while current.left is not None:
            current = current.left
        return current.name, current.bidPrice

    def getHeight(self):
        """
        This function finds the height of the tree.
        :return: int: height of the tree
        """
        if self is None:
            return 0
        right_ans = 0
        left_ans = 0
        if self.left:
            left_ans = self.left.getHeight() + 1
        if self.right:
            right_ans = self.right.getHeight() + 1

        return max(left_ans, right_ans)

    def printMaxtoMin(self):
        """
        This function prints the tree in descending order according to bid price.
        :return: None
        """
        if self.right is not None:
            self.right.printMaxtoMin()
        if self is not None:
            print(self.name, self.bidPrice)
        if self.left is not None:
            self.left.printMaxtoMin()

    def printTreeInOrder(self):
        """
        This function prints the tree in order.
        :return: None
        """
        if self.left is not None:
            self.left.printTreeInOrder()
        if self is not None:
            print(self.name, self.bidPrice)
        if self.right is not None:
            self.right.printTreeInOrder()

    def printTreePostOrder(self):
        """
        This function prints the tree in post order.
        :return: None
        """
        if self.left is not None:
            self.left.printTreePostOrder()
        if self.right is not None:
            self.right.printTreePostOrder()
        if self is not None:
            print(self.name, self.bidPrice)

    def printTreePreOrder(self):
        """
        This function prints the tree in pre-order.
        :return: None
        """
        if self is not None:
            print(self.name, self.bidPrice)
        if self.left is not None:
            self.left.printTreePreOrder()
        if self.right is not None:
            self.right.printTreePreOrder()


company_list = [("rentacar1", 200), ("rentacar2", 300), ("rentacar3", 100), ("rentacar4", 400), ("rentacar5", 150), ("rentacar6", 250),
                ("rentacar7", 320), ("rentacar8", 180), ("rentacar9", 225), ("rentacar10", 380), ("rentacar11", 180), ("rentacar12", 350)]

root = Company(company_list[0][0], company_list[0][1])
for i in range(1, len(company_list)):
    if root.searchSameBidPrice(company_list[i][1]):
        print("Company with same bid price already exists in the tender", company_list[i][0], company_list[i][1])
    else:
        root.joinTender(company_list[i][0], company_list[i][1])

root.printTreeInOrder()
root.withdrawfromTender(225)
print("After withdraw")
root.printTreeInOrder()
print("Winner is", root.findWinner())
print("Height of the tree is", root.getHeight())
print("Descending Order:")
root.printMaxtoMin()





