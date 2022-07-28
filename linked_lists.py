class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        # this is the first node of a linked list (can access this node exclusively)
        self.head = None
        self.num_of_nodes = 0
    
    # O(1)
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        # when linked list is not empty
        else:
        # update the references
            new_node.next_node = self.head
            self.head = new_node

    # O(N) 
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # check emptiness )0
        if self.head is None:
            self.head = new_node
         # when not empty
        else:
            actual_node = self.head
            # why it has O(N) linear running time complexity
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    # O(1)
    def size_of_list(self):
        return self.num_of_nodes


    # O(N)
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node
    
    # O(N)/O(1). we basically omit the node by redirecting the pointers instead of explicitly removing it
    def remove(self, data):
        if self.head is None:
            return 
        
        actual_node = self.head
        # have to track the previous node for future pointer updates
        previous_node = None
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
        
        # search miss
        if actual_node is None:
            return

        # update the references (so we have the data we want to remove)
        # the head note is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remote an internal node by updating the pointers
            # no need to delete the node because the garbage collector will do that = omitting the actual node by redirecting the pointer
            previous_node.next_node = actual_node.next_node
    


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_start(1)
    ll.insert_start(2)
    ll.insert_start(3)
    ll.insert_start(4)
    ll.insert_start(5)
    ll.insert_start(6)
    print(ll.traverse())
    
        