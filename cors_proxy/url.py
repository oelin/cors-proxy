from stack import *


class url(stack):
  
    def __init__(self):
        stack.__init__(self)

    def join(self):
        string = '/'.join(self.stack)

        return string

    def split(self, path):
        segments = path.split('/')

        # Elements filters out all empty strings.

        elements = list(filter(bool, segments))

        return elements

    def changeto(self, path):
        elements = self.split(path)

        for element in elements:
            if (element != '.'):
                if (element == '..'):
                    self.pop()

                elif (element == '/'):
                    self.clear()

                else:
                    self.push(element)
