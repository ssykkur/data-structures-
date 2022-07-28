import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0


class AvlTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            print(f'root node is {self.root.data}')
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, node):
        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self._calc_height(node.left), self._calc_height(node.right)) + 1
                logging.debug(f'inserted left node {node.left.data} and parent height now is {node.height}')
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self._calc_height(node.left), self._calc_height(node.right)) + 1
                logging.debug(f'inserted right node {node.right.data} and parent height now is {node.height}')
        self._balance_check(node)

    def remove(self, data):
        if self.root:
            self._remove(data, self.root)

    def _remove(self, data, node):
        if node is None:
            return

        if data < node.data:
            self._remove(data, node.left)
        elif data > node.data:
            self._remove(data, node.right)
        else:
            parent = node.parent
        
            # leaf
            if node.left is None and node.right is None:
                logging.debug(f'removing leaf node: {node.data}')

                if parent is None:
                    self.root = None
                else:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    self._balance_check(parent)
                del node

            # one left child
            elif node.left is not None and node.right is None:
                logging.debug(f'removing one left child: {node.data}')
                
                if parent is None:
                    node.left.parent = None
                    self.root = node.left
                else:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                    node.left.parent = parent
                    self._balance_check(parent)
                del node

            # one right child
            elif node.left is None and node.right is not None:
                logging.debug(f'removing one right child: {node.data}')

                if parent is None:
                    node.right.parent = None
                    self.root = node.right 
                else:
                    if parent.left == node:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    node.right.parent = parent
                    self._balance_check(parent)
                del node

            # two children
            else:
                logging.debug(f'removing two children: {node.data}')
                predecessor = self._get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self._remove(data, predecessor)

    def _get_predecessor(self, node):
        while node.right:
            node = node.right
        return node

    def _balance_check(self, node):
        while node is not None:
            node.height = max(self._calc_height(node.left), 
                                self._calc_height(node.right)) + 1
            self._enforce_balance(node)
            node = node.parent
    
    def _enforce_balance(self, node):
        balance = self._calc_balance(node)
        logging.debug(f'balance of node {node.data} is {balance}')
        if balance > 1:
            if self._calc_balance(node.left) < 0:
                self._rotate_left(node.left)
            self._rotate_right(node)
        elif balance < -1:
            if self._calc_balance(node.right) > 0:
                self._rotate_right(node.right)
            self._rotate_left(node)
    
    def _rotate_left(self, node):
        logging.debug(f'rotating to left on {node.data} with height: {node.height}')
        temp_right = node.right
        t = temp_right.left
        temp_right.left = node 
        node.right = t

    
        if t:
            t.parent = node

        temp_right.parent = node.parent
        node.parent = temp_right

        if temp_right.parent and temp_right.parent.left == node:
            temp_right.parent.left = temp_right
        if temp_right.parent and temp_right.parent.right == node:
            temp_right.parent.right = temp_right
        
        if node == self.root:
            self.root = temp_right
        
        node.height = max(self._calc_height(node.left), 
                        self._calc_height(node.right)) + 1

        temp_right.height = node.height + 1
        

    def _rotate_right(self, node):
        logging.debug(f'rotating to right on {node.data} with height: {node.height}')
        
        temp_left = node.left
        t = temp_left.right
        temp_left.right = node
        node.left = t

        if t:
            t.parent = node
        
        temp_left.parent = node.parent
        node.parent = temp_left

        parent_left = temp_left.parent
        
        if parent_left and parent_left.left == node:
            parent_left.left = temp_left
        if parent_left and parent_left.right == node:
            parent_left.right = temp_left 
        
        if node == self.root:
            self.root = temp_left
        
        node.height = max(self._calc_height(node.left), 
                        self._calc_height(node.right)) + 1

        temp_left.height = node.height + 1

    def _calc_height(self, node):
        if node is None:
            return - 1
        return node.height

    def _calc_balance(self, node):
        if node is None:
            return 0
        return self._calc_height(node.left) - self._calc_height(node.right)

    def traverse(self):
        if self.root:
            self._traverse(self.root)
    
    def _traverse(self, node):
        if node.left:
            self._traverse(node.left)
        print(node.data)
        if node.right:
            self._traverse(node.right)

    
        
if __name__ == '__main__':
    avl = AvlTree()
    avl.insert(20)
    avl.insert(15)
    avl.insert(16)
    avl.insert(30)
    avl.remove(30)
    avl.traverse()