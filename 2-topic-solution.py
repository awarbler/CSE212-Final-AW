# 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    # to print
    def __str__(self):
        return str(self.value)
        pass