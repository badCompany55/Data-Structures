class Queue:
  def __init__(self):
      self.size = 0
    # what data structure should we
    # use to store queue elements?
      self.storage = []

  def enqueue(self, item):
      self.storage.insert(0, item)
      self.size = len(self.storage)
  
  def dequeue(self):
      if self.size > 0:
          self.size = self.size - 1
          return self.storage.pop()
      else:
          pass

  def len(self):
      if self.size == 0:
          return 0 
      else:
          return self.size


q = Queue()
q.enqueue(100)

print(q.storage)
