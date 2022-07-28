class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0

    # inserts at the end of the linked list
    def insert(self, data):
        new_node = Node(data)

        # empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # at least one
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.previous


dl = DoublyLinkedList()
dl.insert(1)
dl.insert(2)
dl.insert(3)
dl.insert(4)
dl.traverse_forward()
dl.traverse_backward()