class Node:
  def __init__(self, data = None):
      self.data = data
      self.next = self

class CLL:
  def __init__(self):
      self.head = None
      self.count = 0
    
  def append(self, data):
    self.insert(data, self.count)
    return
    
  def insert(self, data, index):
    if (index > self.count) | (index < 0):
        raise ValueError(f"Index out of range: {index}, size: {self.count}")
          
    if self.head == None:
        self.head = Node(data)
        self.count += 1
        return
      
    temp = self.head
    for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
        temp = temp.next
          
    aftertemp = temp.next #New node goes between temp and aftertemp
    temp.next = Node(data)
    temp.next.next = aftertemp
    if(index == 0):
        self.head = temp.next
    self.count += 1
    return
    
  def remove(self, index):
    if (index >= self.count) | (index < 0):
        raise ValueError(f"Index out of range: {index}, size: {self.count}")
      
    if self.count == 1:
        self.head = None
        self.count = 0
        return
      
    before = self.head
    for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
        before = before.next
    after = before.next.next
      
    before.next = after
    if(index == 0):
        self.head = after
    self.count -= 1
    return
    
  def index(self, data):
    temp = self.head
    for i in range(self.count):
        if(temp.data == data):
            return i
        temp = temp.next
    return None
    
  def size(self):
    return self.count
  
  def display(self):
    print(self)