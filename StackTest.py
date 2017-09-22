import unittest
import Stack

class TestStack(unittest.TestCase):

    #create stack object
    def setUp(self):
	self.stack = Stack.Stack()
	self.stack.push([1,2,3])

    #destroy stack object
    def tearDown(self):
	pass

    #test push operation on stack
    def test_push(self):
	self.assertEqual(self.stack.stack[-1], 3)

    #test top operation on stack
    def test_top(self):
	topElement = self.stack.top
	self.assertEqual(topElement, 3)

    #test pop operation on stack
    def test_pop(self):
	self.assertEqual(self.stack.pop(), 3)
	self.assertEqual(self.stack.pop(), 2)
	self.assertEqual(self.stack.pop(), 1)
	self.assertEqual(self.stack.pop(), None)

    
if __name__ == '__main__':
	unittest.main()
