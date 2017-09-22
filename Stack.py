class Stack(object):
  ''' Represents a stack i.e. FILO '''
  def __init__(self):
    self.stack = []    
  
  def push(self, data):
    ''' Pushes the data on the top of the stack '''
    for element in data:
	self.stack.append(element)
    print "Elements added successfully"
  
  def pop(self):
    ''' Removes the data at the top of the stack and return it '''
    if self.stack:
	top = self.stack.pop()
	print str(top)+" removed from stack"
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

if __name__ == '__main__':
    stackObj = Stack()

    stackObj.push([1,2,3,4,5])

    print "Top element: "+str(stackObj.top)

    stackObj.pop()
    stackObj.pop()
    stackObj.pop()
    
