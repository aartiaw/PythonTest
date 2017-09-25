import unittest
import BinaryTree

class TestBinaryTree(unittest.TestCase):

    #create binary tree object
    def setUp(self):
	self.tree = BinaryTree.BinaryTree()
	data = [5,2,6,1,3]
        for i in data:
	   self.tree.insert(i)
	
    #destroy tree object
    def tearDown(self):
	pass

    #test insert function on tree by checking root element
    def test_insert(self):
	self.assertEqual(self.tree.get_root(), 5)

    #test find element from tree
    def test_find(self):
	self.assertEqual(self.tree.find(2), 2)

    #test level order
    def test_level_order(self):
	self.assertEqual(self.tree.level_order(), [5, 2, 6, 1, 3])

    #test inorder
    def test_inorder(self):
	self.assertEqual(self.tree.inorder(), [1, 2, 3, 5, 6])

    #test preorder
    def test_preorder(self):
	self.assertEqual(self.tree.preorder(), [5, 2, 1, 3, 6])

    #test postorder
    def test_postorder(self):
	self.assertEqual(self.tree.postorder(), [1, 3, 2, 6, 5])

    
#execute test cases    
if __name__ == '__main__':
	unittest.main()
