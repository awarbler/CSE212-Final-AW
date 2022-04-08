# Binary Tree

A binary tree is a type of data structure that is nonlinear with a hierarchical relationship between elements without having a cycle. It is connected with edges.
A binary tree can be used in a café situation in a real-life case. On the menu, drinks are separated into hot beverages and cold beverages. Binary trees have nodes and each not has two children. There are left or right children in the tree. 

## Purpose

Binary trees are easier and quicker to access data. Binary trees are used to parse problems. 

## Types

|     Term    |     Definition    |
|---|---|
|    Full Binary Tree    |    Points to zero nodes or the max of two nodes     |
|    Perfect Binary Tree    |    All nodes have two children and all leafs are located on the same level    |
|    Complete Binary Tree   |    Filling tree from left to right with no gaps  |
|    Balanced Binary Tree    |     Remove a node from the list.         |
|    Binary Search Tree    |     Nodes are compared to the root and sort by less or greater          |


## Terminology

Table 1.2 explains the basic definitions for Linked List
|     Term    |     Definition    |
|---|---|
|     Base category    |  It is the first category   |
|     Nodes  |  Point at other nodes   |
|     Child Node    |    It is under the parent node   |
|     Edge    |    It is the link between the parent and the child   |
|     Leaf   |    Is a node that does not have a child   |
|     Parent Node    |     It is the first node in a subcategory  |
|     Root Node    |     The first Node does not have a parent |
|     Sibling  |   Is the children of the same parent, a sibling can only have one parent |
|     Depth  |   The length of the path of the root to the node  |
|     Height  |   The length of the path from the root to the deepest node   |



## Operations

|     Term    |     Definition    |
|---|---|
|     Insert    |     Add a node to any location, beginning, middle, end    |
|     Traversal    |     Traverse all of the nodes from beginning to end.    |
|     Searching    |     Search the value of an element    |
|     deletion    |     Remove a node from the list.         |
|     Sort    |     Sort the Node of the linked list.    |

## Examples

```python
 def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

```

## Problem

In our family history class we need to find the first common ancestor. Use a binary tree to find it. Avoid storing any additonal nodes in a data structure. 


### Before Coding

- List test cases and their answers
- Consider the problems.
- Evaluate your code against all test cases
- Do not Rush to Code
- Make code simple and shortcode
- Sketch everything on paper first
- Draw out sketches
- Pick out clear names
- Reuse code
- In the algorithm, make sure you handle all run time errors in logic


### Solve

You can check your code with the solution here: [Solution](2-topic-solution.py)

[Back to Welcome Page](0-welcome.md)

Works Cited
