from Queue import Queue
from Stack import Stack


class BinaryTree(object):

    ''' Represents a binary tree '''
    class Node(object):
        ''' Represents a node in the binary tree '''
        def __init__(self, data):
            ''' Constructor for Node '''
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        ''' Constructor for Binary Tree '''
        self.root = None

    def get_root(self):
        ''' Returns root element '''
        return self.root.data

    def insert(self, data):
        ''' Insert a node in tree '''
        node = self.Node(data)
        ''' Create root node initially '''
        if self.root is None:
            self.root = node
        else:
            head = self.root
            while True:
                ''' When data < root.data and root.left is empty, add
                node to the left of root.
                '''
                if data < head.data:
                    if head.left is None:
                        head.left = node
                        break
                    head = head.left
                ''' When data > root.data and root.left is empty,
                add node to the left of root.
                '''
                if data > head.data:
                    if head.right is None:
                        head.right = node
                        break
                    head = head.right

    def find(self, data):
        ''' Search for data in the tree '''
        node = self.root
        ''' Iterate whole tree to find if data exists,
        if found, return the data, else give appropriate message.
        '''
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
        ''' Breadth first traversal of tree '''
        queue = Queue()
        queue.enqueue(self.root)
        levelorder = []
        ''' Display root node, enqueue it's left and right node. For all
        elements enqueued, put it's left and right nodes in the queue.
        Dequeue the queue to get level order of tree.
        '''
        while queue.queue:
            node = queue.dequeue()
            if node:
                levelorder.append(node.data)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        return levelorder

    def inorder(self):
        ''' Iterative inorder traversal '''
        if self.root is None:
            return
        stack = Stack()
        inorder = []
        node = self.root
        ''' Starting with root node, traverse and push left subtree in the stack.
        Push root in the stack and then push right subtree into the stack.
        Pop the stack to get inorder traversal of tree.
        '''
        while stack.stack or node:
            if node:
                stack.push(node)
                node = node.left
            else:
                node = stack.pop()
                inorder.append(node.data)
                node = node.right
        return inorder

    def preorder(self):
        ''' Iterative preorder traversal '''
        stack = Stack()
        stack.push(self.root)
        preorder = []
        ''' Pop root node from the stack. Push it's left subtree and
        then right subtree into the stack. Pop the top of the stack
        to get preorder traversal.
        '''
        while stack.stack:
            node = stack.pop()
            preorder.append(node.data)
            if node.right:
                stack.push(node.right)
            if node.left:
                stack.push(node.left)
        return preorder

    def postorder(self):
        ''' Iterative postorder traversal '''
        postorder = []
        stack = Stack()
        visited = None
        current = self.root
        ''' Push left subtree of the root into the stack. Push the
        right subtree of all elements of the stack. Pop the stack
        to get postorder traversal.
        '''
        while stack.stack or current is not None:
            if current is not None:
                stack.push(current)
                current = current.left
            else:
                middle = stack.stack[len(stack.stack)-1]
                if middle.right is None or visited == middle.right:
                    postorder.append(middle.data)
                    visited = stack.pop()
                else:
                    current = middle.right
        return postorder


''' Executing above functions '''
if __name__ == '__main__':
    binaryTreeObj = BinaryTree()
    ''' Insert data into binary tree '''
    data = [5, 2, 6, 1, 3]
    for i in data:
        binaryTreeObj.insert(i)

    ''' Search for given element, here 2 '''
    print binaryTreeObj.find(2)

    ''' Display level order traversal '''
    print 'Level order traversal'
    print binaryTreeObj.level_order()

    ''' Display inorder traversal '''
    print 'Inorder traversal'
    print binaryTreeObj.inorder()

    ''' Display preorder traversal '''
    print 'Preorder traversal'
    print binaryTreeObj.preorder()

    ''' Display postorder traversal '''
    print 'Postorder traversal'
    print binaryTreeObj.postorder()

