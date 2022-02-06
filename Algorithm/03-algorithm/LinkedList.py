class Node:
    """ Node class """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """ LinkedList object """

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node



# Create a linked list
llist = LinkedList()

# Inserting nodes to the linked list
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

# Link first node to second node
llist.head.next = second
second.next = third
third.next = fourth

print(llist.printList())