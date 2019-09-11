class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      node = BinarySearchTree(value)
      if value < self.value:
          if self.left:
              self.left.insert(value)
          else:
              self.left = node
      else:
          if self.right:
              self.right.insert(value)
          else:
              self.right = node

  def contains(self, target):
      if self.value == target:
          return True
      if target < self.value:
          if self.left:
              return self.left.contains(target)
          else:
              return False
      else:
          if self.right:
              return self.right.contains(target)
          else:
              return False

  def get_max(self):
      if self.right is None:
          return self.value
      if self.right:
          return self.right.get_max()

  def for_each(self, cb):
      cb(self.value)
      if self.right:
          self.right.for_each(cb)
      if self.left:
          self.left.for_each(cb)


bst = BinarySearchTree(0)
bst.insert(7)
bst.insert(5)
print(bst.contains(7))
