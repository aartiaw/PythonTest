import unittest
import Queue

class TestQueue(unittest.TestCase):

    #create queue object
    def setUp(self):
	self.queue = Queue.Queue()
	self.queue.enqueue([1,2,3])

    #destroy queue object
    def tearDown(self):
	pass

    #test enqueue operation on queue
    def test_enqueue(self):
	self.assertEqual(self.queue.queue[-1], 3)

    #test front operation on queue
    def test_front(self):
	frontElement = self.queue.front
	self.assertEqual(frontElement, 1)

    #test dequeue operation on queue
    def test_dequeue(self):
	self.assertEqual(self.queue.dequeue(), 1)
	self.assertEqual(self.queue.dequeue(), 2)
	self.assertEqual(self.queue.dequeue(), 3)
	self.assertEqual(self.queue.dequeue(), None)

    
if __name__ == '__main__':
	unittest.main()
