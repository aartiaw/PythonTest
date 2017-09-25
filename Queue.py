class Queue(object):
  ''' Represents a queue i.e. FIFO '''
  
  def __init__(self):
    self.queue = []
  
  def enqueue(self, data):
    ''' Adds the data at the end of the queue '''
    self.queue.append(data)
    
  
  def dequeue(self):
    ''' Remove the data from the front of the queue and return it '''
    if self.queue:
        element = self.queue.pop(0)
        return element
    else:
        return
  
  @property
  def front(self):
    ''' Returns the data at the front of the queue '''
    if self.queue:
    	return self.queue[0]
    else:
	return


'''Executing above functions'''
if __name__ == '__main__':
    queueobj = Queue()

    '''Insert elements into queue'''
    data = [1,2,3,4,5]
    for element in data:
	queueobj.enqueue(element)
    
    '''Print front element from queue'''    
    print "Front element: "+str(queueobj.front)
    
    '''Dequeue elements from rear of the queue'''
    queueobj.dequeue()
    queueobj.dequeue()
    queueobj.dequeue()
    

    

