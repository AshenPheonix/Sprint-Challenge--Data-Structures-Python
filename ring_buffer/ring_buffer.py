class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #test to see if I'm at capcity
    if self.current==self.capacity:
      #if I am, reset current
      self.current=0

    #store item in current location
    self.storage[self.current]=item
    #return 
    self.current+=1

  def get(self):
    #copy contents of array
    temp_array = [i for i in self.storage]
    #remove Nones
    while None in temp_array:
      temp_array.remove(None)
    
    #return
    return temp_array