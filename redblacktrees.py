import logging


logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')


class Color:

    RED = 1
    BLACK = 2


class Node:

    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None


class RedBlackTree:

    def __init__(self):
        self.root = None
    
    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
            self.settle_violation(self.root)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):

        if data < node.data:
            if node.left:
                self._insert(data, node.left)
            else:
                node.left = Node(data, node)
                logging.debug(f'inserted left node {node.left.data}')
                self.settle_violation(node.left)
        else:
            if node.right:
                self._insert(data, node.right)
            else:
                node.right = Node(data, node)
                logging.debug(f'inserted right node {node.right.data}')
                self.settle_violation(node.right)

    def traverse(self):

        if self.root:
            self._traverse(self.root)

    def _traverse(self, node):

        if node.left:
            self._traverse(node.left)

        print(node.data)

        if node.right:
            self._traverse(node.right)

    def rotate_right(self, node):
        logging.debug(f'right rotation on {node.data}')

        temp_left = node.left
        t = temp_left.right

        temp_left.right = node
        node.left = t

        if t:
            t.parent = node
        
        temp_parent = node.parent
        temp_left.parent = temp_parent
        node.parent = temp_left
        
        parent = temp_left.parent

        if parent:
            if parent.left == node:
                parent.left = temp_left
            else:
                parent.right = temp_left
        else:
            self.root = temp_left
        

    def rotate_left(self, node):
        logging.debug(f'left rotation on {node.data}')

        temp_right = node.right
        t = temp_right.left

        temp_right.left = node
        node.right = t

        if t:
            t.parent = node
        
        temp_parent = node.parent
        node.parent = temp_right
        temp_right.parent = temp_parent
        
        parent = temp_right.parent

        if parent:
            if parent.left == node:
                parent.left = temp_right
            else:
                parent.right = temp_right
        else:
            self.root = temp_right

    def settle_violation(self, node):

        while self.is_red(node.parent):
            parent_node = node.parent
            grandparent_node = parent_node.parent
            if parent_node == grandparent_node.left:
                uncle = grandparent_node.right
                
                # CASE 1. UNCLE IS RED 
                if uncle and self.is_red(uncle):

                    logging.debug(f'case 1 on {node.data}')
                    logging.debug(f'recoloring node "{grandparent_node.data}" to red')

                    grandparent_node.color = Color.RED

                    logging.debug(f'recoloring node "{parent_node.data}" to black')
                    logging.debug(f'recoloring node "{uncle.data}" to black')

                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grandparent_node
                else: 
                    # CASE 2. UNCLE IS BLACK OR NULL + NODE IS THE RIGHT CHILD 
                    # OF THE PARENT
                    if node == parent_node.right:

                        logging.debug(f'case 2 on {node.data}')

                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent
                        

                    # CASE 3. UNCLE IS BLACK 
                    logging.debug(f'case 3 on {node.data}')
                    logging.debug(f'recoloring {parent_node.data} to black')
                    logging.debug(f'recoloring {grandparent_node.data} to red')

                    parent_node.color = Color.BLACK
                    grandparent_node.color = Color.RED
                    self.rotate_right(grandparent_node)

            else:
                uncle = grandparent_node.left

                if uncle and self.is_red(uncle):

                    logging.debug(f'case 1 on {node.data}')
                    logging.debug(f'recoloring node "{grandparent_node.data}" to red')
                    logging.debug(f'recoloring node "{parent_node.data}" to black')
                    logging.debug(f'recoloring node "{uncle.data}" to black')

                    grandparent_node.color = Color.RED
                    parent_node.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = grandparent_node
                else:
                    if node == parent_node.left:

                        logging.debug(f'case 2 on {node.data}')

                        self.rotate_right(node)
                        node = parent_node
                        parent_node = node.parent
                    
                    logging.debug(f'case 3 on {node.data}')
                    logging.debug(f'recoloring {parent_node.data} to black')
                    logging.debug(f'recoloring {grandparent_node.data} to red')

                    parent_node.color = Color.BLACK
                    grandparent_node.color = Color.RED
                   
                    self.rotate_left(grandparent_node)

        if self.is_red(self.root):
            logging.debug(f'Recoloring the root {self.root.data} to black')

            self.root.color = Color.BLACK

    def is_red(self, node):
    
        if node is None:
            return False

        return node.color == Color.RED


    
if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(32)
    rbt.insert(10)
    rbt.insert(55)
    rbt.insert(1)
    rbt.insert(19)
    rbt.insert(79)
    rbt.insert(16)
    rbt.insert(23)
    rbt.insert(12)

    