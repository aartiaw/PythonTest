class BinaryTree(object):
  ''' Represents a binary tree '''
  
  class Node(object):
    ''' Represents a node in the binary tree '''
        
    def __init__(self, data):
      ''' Constructor for Node '''
      self.data = data
      self.left = None
      self.right = None

    def __str__(self):
            return "[{0}<-{1}->{2}]".format(self.left, self.data, self.right)
     
  
  def __init__(self):
    ''' Constructor for Binary Tree '''
    self.root = None

  def getRoot(self):
    ''' Returns root element '''
    return self.root.data
  
  def insert(self, data):
    '''Insert a node in tree'''
    node = self.Node(data)
    if self.root is None:
	self.root = node

    else:
	head = self.root
	while True:
	    if data < head.data:
		if head.left is None:
		   head.left = node
		   break
		head = head.left

	    elif data > head.data:
		if head.right is None:
		   head.right = node
		   break
		head = head.right 
 	   	  

  def find(self, data):
    node = self.root
    
    while node:
	if node.data == data:
	    return node.data
        else:
	    if data < node.data:
		node = node.left
	    else:
		node = node.right
    print "This value does'nt exists"
    return
  

  def level_order(self):
    '''Breadth first traversal of tree'''
    queue = [self.root]
    testlist = []
    while queue:
	node = queue.pop(0)
	testlist.append(node.data)

	if node.left is not None:
	    queue.append(node.left)
	if node.right is not None:
	    queue.append(node.right)

    return testlist
  

  def inorder(self):
    '''Iterative inorder traversal'''
    if self.root is None:
	return
    stack = []
    testlist = []
    node = self.root
    
    while stack or node:
            if node:
		stack.append(node)                
		node = node.left
		
            else:
                node = stack.pop()
		testlist.append(node.data)
                node = node.right
    
    return testlist
  
  def preorder(self):
    stack = [self.root]
    testlist = []

    while stack:
        node = stack.pop()
        testlist.append(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return testlist
  
  def postorder(self):
    testlist = []
    list = []
    visited = None
    current = self.root

    while len(list) > 0 or current is not None:
        if current is not None:
            list.append(current)
            current = current.left
        else:
            middle = list[len(list)-1]
            if middle.right is None or visited == middle.right:
                testlist.append(middle.data)
                visited = list.pop(len(list)-1)
            else:
                current = middle.right

    return testlist


if __name__ == '__main__':
    binaryTreeObj = BinaryTree()
    
    data = [5,2,6,1,3]
    for i in data:
	binaryTreeObj.insert(i)

    print binaryTreeObj.find(2)

    print 'Level order traversal'
    print binaryTreeObj.level_order()

    print 'Inorder traversal'
    print binaryTreeObj.inorder()

    print 'Preorder traversal'
    print binaryTreeObj.preorder()

    print 'Postorder traversal'
    print binaryTreeObj.postorder()

    

