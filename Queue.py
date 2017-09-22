class Queue(object):
  ''' Represents a queue i.e. FIFO '''
  
  def __init__(self):
    self.queue = []
  
  def enqueue(self, data):
    ''' Adds the data at the end of the queue '''
    for element in data:
	self.queue.append(element)
    print "Elements added successfully"
  
  def dequeue(self):
    ''' Remove the data from the front of the queue and return it '''
    if self.queue:
        element = self.queue.pop(0)
        print str(element)+" removed from queue"
	return element
    else:
        print "Queue is empty"
  
  @property
  def front(self):
    ''' Returns the data at the front of the queue '''
    if self.queue:
    	return self.queue[0]
    else:
	return


if __name__ == '__main__':
    queueObj = Queue()

    queueObj.enqueue([1,2,3,4,5])
        
    print "Front element: "+str(queueObj.front)
    
    queueObj.dequeue()
    queueObj.dequeue()
    queueObj.dequeue()
    

    

