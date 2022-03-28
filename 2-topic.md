# Linked List

A linked list is a data structure form of a sequential collection of elements, and it does not have to be in order. A linked list is made up of independent nodes that contain data. A linked list is like a train. It has many compartments. Each department (Node) is a connected compartment, and it holds people. If we need to add or delete a node, we can add in the beginning, the middle, or the end. If we want to see what is in the compartments, we must traverse through each one sequentially. Each element or Node has two parts: data and reference to the next Node. A linked list memory is not contagious; therefore, it is essential to use the link pointer of the head or the tail.

## Purpose

A linked list is helpful in video games with more than one player. Once everyone has a turn, they have the option to start back at the first player until a winner is declared. A double-linked is incorporated on an iPhone music playlist, and we may play one song. We could play the previous song or the next song if we wanted to.

## Linked List vs. Arrays

A linked list is a data structure, and an array is not a data structure. Arrays and linked lists technically can do the same such as insertion, addition, and removal. The main difference between a linked list and an array is that a linked list is that each element in a linked list is independent of the other. In arrays, the data elements are not separate objects, so we cannot delete a cell, we can delete the value of the cell, but the cell will remain in memory. Unlike arrays, a linked list is efficient because we do not have to change each index when we insert and remove it. Arrays are great for finding items, but linked lists are better at insertions and removals.

## Types

|     Term    |     Definition    |
|---|---|
|     Single Linked List    |     each Node stores the value and points to the next Node. It does not have any pointer to the previous Node. Each Node has two parts. The first part is the value, and the second part is the pointer or reference. The last Node is always null. The first Node points to the second Node. Flexible to add and remove nodes at run time. It cannot go back to the first Node.     |
|     Double Linked List    |     A double-linked list Resembles a single linked list. A double-linked list has two pointers from each Node and a value. It references the previous Node, and it references the next Node. Traverse backward and forward.     |
|     Circular Singly Linked List     |     Same as a single linked list, except the last node of the list stores a pointer/ reference to the first Node. The head has a physical location stored in the tail or last Node. If we traverse through the linked list, we have an option to visit the first Node. A circular, singly linked list creates a circle.     |
|     Circular Double Linked List    |     It is the same as a circular single-linked list, except it is accessible to traverse forward and backward. Loop indefinitely.     |

## Structure

- Insert Picture

## Terminology

Table 1.2 explains the basic definitions for Linked List
|     Term    |     Definition    |
|---|---|
|     Node    |     It is an element in a linked list. There are two parts to a node. The first part holds data second holds a reference of memory called a pointer.       |
|     Head    |     The head refers to the first Node in the linked list.     |
|     Tail    |     The name of the last Node in the linked list. The pointer usually points to the tail and is empty     |
|     Pointer    |     Allocate where a node is in memory. The physical address of the next. Node is stored in the previous node pointer.    |
|     Next     |     A pointer in the Node refers to the next Node.     |
|     Value    |     The actual data in the Node.     |
|     Previous    |     A pointer in the Node referring to the previous Node    |

## Operations

|     Term    |     Definition    |
|---|---|
|     Insertion    |     Add a node to any location, beginning, middle, end    |
|     Traversal    |     Traverse all of the nodes from beginning to end.    |
|     Searching    |     Search the value of an element    |
|     deletion    |     Remove a node from the list.         |
|     Sort    |     Sort the Node of the linked list.    |

## Example Linked List

Three steps to create a Single Linked list:
    - Create Head and Tail, initialize with null
    - Create a blank Node and assign a value and reference with null
    - Link Head and tail with Node

1.Create a linked list
    - Create a class Single linked list(parameter of self)
    - Create/ initialize head and tail with null/none references
    - Create a node with null/none reference
    - Create a pointer - this creates a link between the first Node and head.
    - Time Complexity O(1)

``` python
        class SingleLinkList:
  #Initialize  and call self
            def __init__(self):
                self.head = None
     self.tail = None
 ```

2.Create a class for nodes
    - initialize class Node
    - Set value and next
    - Time Complexity O(1)

``` python
        class Node:
  #Initialize call self and value
            def __init__(self):
                self.value = None
     self.next = None
```

3.Create a linked list
    - Use singleLinkeList and Nodes class
    - Create two nodes
    - Link together
    - Assign the first node to the head value of the linked list
    - Time complexity is O(1)

```python

        sLL = SingleLinkList()
  node1 = Node(1)
  node2 = Node(2)
  sLL.head = node1 # assigning head
  sLL.head.next = node2 # assigning next node
  sLL.tail = node2 # assigning tail

```

4.Create a method that will help us run and print our test.
    - Print out the queue correctly
    - Time Complexity O(1)

```python
        def __str__(self):
            values = [str(x) for x in self.items]
            return ' '.join(values)
```

## Problem

Our music on our iPod will not play the previous song.

You can check your code with the solution here: [Solution](2-topic-solution.py)

[Back to Welcome Page](0-welcome.md)

Works Cited
<https://www.123rf.com/photo_128160367_stock-vector-passenger-tram-train-realistic-mockup-with-side-view-of-three-metropolitan-trains-with-various-color.html>

<https://www.dreamstime.com/train-tram-subway-wagons-side-view-metro-locomotive-rails-isolated-modern-commuter-city-transport-railway-vehicle-modes-image226814646>
<https://www.programiz.com/dsa/linked-list-operations>
