# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:57:50 2018

@author: sanooj
"""

"""
TREE
"""
"""
root

leaves

node
--- key
--- payload

edge
-----

# connects two nodes

path
-----

# ordered list of nodes that are connected by edges


children
---------

set of nodes "c" -> that have incoming edges from the same node
 

parent
---------

a node is the parent of all the nodes it
connects to with outgoing edges

Sibling
-------

children of the same parent are said to be siblings

Subtree
-------

set of nodes and edges comprised of a parent
and all the descendants of that parent

Leaf node
---------

node with no children

Level
-----

n ->

number of edges on the path from the root node to "n"


Height
-------

maximum level of any node in the tree


"""



"Tree with lists"

"""
Binary Tree
"""
"""
                a
               -  -
               |  |
               b  c  
             --   --
             | |  |
             d e  f 



my_tree = 
[
["a",
[  ["b", [  "d" , [],[] ],[ "e" , [], [] ]  ]  ],
[  "c", [ ["f" , [] , [] ]  ], []   ]
]
]



"""

"""
TREE WITH LISTS
"""

class BinaryTreeWithList(object):
    
    def __init__(self,payload):
        self._root = self.make_binary_tree(payload)
       
    @property
    def root(self):
        return self._root
    
    @root.getter
    def root(self):
        return self._root
    
    @root.setter
    def root(self,value):
        self._root = value
    
    
    def make_binary_tree(self,payload):
         return [payload, [], []]
     
    def insert_left(self,root: list,new_branch_payload):
           
        #left branch is index 1
        # right branch its at index 2
        
        # get left branch
        left_branch = root.pop(1)
        
        # new branch
        new_branch = self.make_binary_tree(new_branch_payload)
        
        # add left_branch to the left of new_branch
        new_branch[1] = left_branch
        
        # add to root as the new left_branch
        root.insert(1,new_branch)
        
        return new_branch
        
    def insert_right(self,root: list,new_branch_payload):
        
        # get right branch
        # left_branch at index 1
        # right_branch at index 2
        right_branch = \
        root.pop(2)
        
        new_branch = \
        self.make_binary_tree(new_branch_payload)
        
        new_branch[2] = \
        right_branch
        
        root.insert(2,new_branch)
        
        return new_branch
        
    def get_root_val(self):
        return self.root[0]
    
    def set_root_val(self,payload:object):
        self.root[0] = payload
        
    def get_left_child(self,branch:list):
        return branch[1]
    
    def get_right_child(self,branch:list):
        return branch[2]
    
def testBinaryTreeWithList():
    """  
    Binary Tree


                a
               -  -
               |  |
               b  c  
             --   --
             | |  |
             d e  f 
    """
    
    binaryTree = BinaryTreeWithList("a")
    print(binaryTree.root) 
    #['a', [], []]
    
    new_branch_c = \
    binaryTree.insert_right(binaryTree.root,"c")
    print(binaryTree.root)
     #['a',[],[    ['c'],[],[]   ]
     
    binaryTree.insert_left(new_branch_c,"f")
    print(binaryTree.root)
    
    new_branch_b = \
    binaryTree.insert_left(binaryTree.root,"b")
    print(binaryTree.root)
     #['a',[  ['b'],[],[]       ],[    ['c'],[],[]   ]
    
    
    binaryTree.insert_left(new_branch_b,"d")
    print(binaryTree.root)
     #['a',[    ['b'],[   [ 'd' ],[],[]    ],[]    ],[    ['c'],[],[]   ]
     
    binaryTree.insert_right(new_branch_b,"e")
    print(binaryTree.root)
     #['a',[    ['b'],[   [ 'd' ],[],[]    ],[    ['e'],[],[]     ]    ],[    ['c'],[  ['f'],[],[]         ],[]   ]
    

    
testBinaryTreeWithList()
    