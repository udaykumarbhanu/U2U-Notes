""" Binary Search Tree(BST): 
Most important properties are: 
1. The left subtree of a node contains only nodes with keys less than the node’s key.
2. The right subtree of a node contains only nodes with keys greater than the node’s key.
3. The left and right subtree each must also be a binary search tree.

Note: There must be no duplicate nodes.
"""

# BST Node. A BST can be made using nodes i.e. vertices. 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

"""
1. Searching a key:
To search a given key in BST, we first compare it with root, if the key is present at root,
we return root. If key is greater than root’s key, we recur for right subtree of root node. 
Otherwise we recur for left subtree.
"""
def search(root, key):     
    # Base Cases: root is None or root and key are SAME.
    if root is None or root.val == key:
        return root
 
    # Key is GREATER than root's key.
    if root.val < key:
        return search(root.right, key)     
 	
   	else: # Key is SMALLER than root's key.
    	return search(root.left, key)

""" 
2. Inserting a key:
A new key is always inserted at leaf. We start searching a key from root till we hit a 
leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.
"""
def insert(root, node):
	# Base case: When root is None, new node will become root.
    if root is None:
        root = node
    else:
    	# When new key is GREATER than root.
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        # When new key is LESS than root.
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

""" Time Complexity: The worst case time complexity of search and insert operations is
O(h) where h is height of BST.
"""

"""
3. Print the BST tree:
There are three ways in which a BST can be displayed: (a) Inorder, (b) Pre-order and 
(c) Post-order.
If expression: a+b is a BST. 
Inorder output: print a, print +, print b
Pre-order output: print +, print a, print b
Post-order output: print a, print b, print +
"""
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def pre-order(root):
    if root:        
        print(root.val)
        inorder(root.left)
        inorder(root.right)

def post-order(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.val)

"""
3. Delete a node in BST:
A node deletion operation in BST is a bit different.
3.1 Node to be deleted is leaf: Simply remove from the tree.
3.2 

"""


"""
Important tips for BST: 
1. Inorder traversal of BST always produces sorted output.
2. We can construct a BST with only Preorder or Postorder or Level Order traversal.
"""
