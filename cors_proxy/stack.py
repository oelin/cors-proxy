class stack(object):
    def __init__(self):
        # The stack is a list object

       self.stack = list()

    # Remove and return the last element in the stack.

    def pop(self):
        element = self.stack.pop()

        return element

    # Add an element to end of the stack.

    def push(self, element):
       self.stack.append(element)

    def clear(self):
       self.stack.clear()
