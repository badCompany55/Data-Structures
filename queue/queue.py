import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
# class Queue:
#   def __init__(self):
#       self.size = 0
#     # what data structure should we
#     # use to store queue elements?
#       self.storage = []
#
#   def enqueue(self, item):
#       self.storage.insert(0, item)
#       self.size = len(self.storage)
#   
#   def dequeue(self):
#       if self.size > 0:
#           self.size = self.size - 1
#           return self.storage.pop()
#       else:
#           pass
#
#   def len(self):
#       if self.size == 0:
#           return 0 
#       else:
#           return self.size


d_link_list = DoublyLinkedList()

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = d_link_list

    def enqueue(self, item):
        self.size += 1
        self.storage.add_to_tail(item)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return

    def len(self):
        return self.size


test = Queue()


