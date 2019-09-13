class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
      self.storage.append(value)
      the_index = len(self.storage) - 1
      self._bubble_up(the_index)

  def delete(self):
    if len(self.storage) == 1:
          deleted = self.storage.pop()

    elif len(self.storage) > 1:
          self.storage[0], self.storage[len(self.storage) - 1] = self.storage[len(self.storage) - 1], self.storage[0]
          deleted = self.storage.pop()
          self._sift_down(0)
    else:
        deleted = False
    return deleted

  def get_max(self):
      return self.storage[0]

  def get_size(self):
      return len(self.storage)

  def _bubble_up(self, index):
      child_i = index
      parent_i = (child_i - 1) // 2
      while parent_i >= 0:
          i = self.storage
          parent = i[parent_i]
          child = i[child_i]
          if child > parent:
              i[child_i], i[parent_i] = i[parent_i], i[child_i]
              child_i = parent_i 
              parent_i = (child_i - 1) // 2
          else:
              break

  def _sift_down(self, index):
      max_index = self.get_size() - 1
      max_child = self._max_child(index)

      # check if a child exist within the array first
      if max_child > max_index:
          return
      elif self.storage[index] < self.storage[max_child]:
          self.storage[index], self.storage[max_child] = self.storage[max_child], self.storage[index]
          return self._sift_down(max_child)
      else:
          return

  def _max_child(self, index):
      """
        Returns the index of the max child of a parent
      """
      max_index = self.get_size() - 1
      left_child_index = (index * 2) + 1
      right_child_index = (index * 2) + 2

      # check to see if there is a right child that fits inside the array
      if right_child_index > max_index:
          return left_child_index
      else:
          # check to see which if the two is the max child
          if self.storage[left_child_index] >= self.storage[right_child_index]:
              return left_child_index
          else:
              return right_child_index
heap = Heap()


heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)
heap.delete()
print(heap.storage)

#
# heap.insert(6)
# heap.insert(7)
# heap.insert(5)
# heap.insert(8)
# heap.insert(10)
# heap.insert(1)
# heap.insert(2)
# heap.insert(5)

# descending_order = []
#
# while heap.get_size() > 0:
#     descending_order.append(heap.delete())
#     print(descending_order)
