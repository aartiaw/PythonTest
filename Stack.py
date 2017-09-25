class Stack(object):
  ''' Represents a stack i.e. FILO '''
  def __init__(self):
    self.stack = []    
  
  def push(self, data):
    ''' Pushes the data on the top of the stack '''
    self.stack.append(data)
      
  def pop(self):
    ''' Removes the data at the top of the stack and return it '''
    if self.stack:
	top = self.stack.pop()
	return top
    else:
	print "Stack is empty"
	return  

  @property
  def top(self):
    ''' Returns the data at the top of the stack '''
    if self.stack:
	top = self.stack[-1]
	return top
    else:
	return 

'''Executing above functions'''
if __name__ == '__main__':
    stackobj = Stack()

    '''Insert elements into stack'''
    data = [1,2,3,4,5]
    for element in data:
        stackobj.push(element)

    '''Print top element from stack'''
    print "Top element: "+str(stackobj.top)

    '''Pop elements from the top of the stack'''
    stackobj.pop()
    stackobj.pop()
    stackobj.pop()
    
