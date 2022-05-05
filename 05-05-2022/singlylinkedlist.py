class Node:
  def __init__(self,data,next=None):
    self.data = data
    self.next = next

class S_linked_list:
  def __init__(self):
    self.head = None
    self.tail = None

  def len_list(self):
    length = 0
    ele = self.head
    while ele:
      length += 1
      ele = ele.next
    return length
  
  def push(self,element):
    if self.head == None:
      self.tail = self.head = Node(element)
    else: 
      self.tail.next = Node(element)
      self.tail = self.tail.next
    return self.tail
  
  def insert_at_head(self,element):
    self.head = Node(element,self.head)
    return self.head

  def insert_multipple_values(self,element_list):
    for element in element_list:
      self.push(element)
    def insert_at(self, index, data):
      if index<0 or index>self.len_list():
          raise Exception("Invalid Index")

      if index==0:
          self.insert_at_begining(data)
          return

      count = 0
      itr = self.head
      while itr:
          if count == index - 1:
              node = Node(data, itr.next)
              itr.next = node
              break

          itr = itr.next
          count += 1
  
  def pop(self):
    if self.head == None:
      return "Linked list is empty"
    else:
      self.head = self.head.next
    return self.head
  

  def remove_at(self, index):
      if index<0 or index>=self.len_list():
          raise Exception("Invalid Index")

      if index==0:
          self.head = self.head.next
          return

      count = 0
      itr = self.head
      while itr:
          if count == index - 1:
              itr.next = itr.next.next
              break

          itr = itr.next
          count+=1

  def display_list(self):
    if self.head == None:
      return "linked list is empty"
    
    ele = self.head
    linked_list = ""
    
    while ele:
      linked_list += f"({ele.data},{ele.next})" 
      ele = ele.next
    
    print(linked_list)

  def search(self,element):
    if self.head == None:
      return "list is empty"

    count = 0
    ele = self.head
    while ele:
      if ele.data == element:
        return count
      
      ele = ele.next
      count += 1

obj = S_linked_list()
obj.insert_multipple_values([5,6,7])
print(obj.len_list())
obj.insert_at(1,2)
obj.remove_at(2)
obj.display_list()