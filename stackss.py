# LIFO 
class Stack:

    def __init__(self):
        self.stack = []

    # O(1)
    def push(self, data):
        self.stack.append(data)

    # O(1)
    def pop(self):
        if self.stack_size() < 1:
            return 
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


