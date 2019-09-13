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

# depth first traversal
# =======================================================
  def for_each(self, cb):
      cb(self.value)
      if self.right:
          self.right.for_each(cb)
      if self.left:
          self.left.for_each(cb)

# depth first traversal
# =======================================================
  def dft_non_recursive(self, cb):
      stack = []
      stack.append(self)

      while stack:
          current_node = stack.pop()
          if current_node.left:
              stack.append(current_node.left)
          if current_node.right:
              stack.append(current_node.right)

          cb(current_node.value)

# depth first traversal "can't be recursive"
# =======================================================
def bft_for_each(self, cb):
    q = Queue()
    q.enqueue(self)
    while(q):
        current_node = q.dequeue()
        if current_node.left:
            q.enqueue(current_node.left)

        if current_node.right:
            q.enqueue(current_node.right)

        cb(current_node.value)


bst = BinarySearchTree(0)
bst.insert(7)
bst.insert(5)
print(bst.contains(7))
