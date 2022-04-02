# Linked List

A linked list is a data structure form of a sequential collection of elements, and it does not have to be in order. A linked list is made up of independent nodes that contain data. A linked list is like a train. It has many compartments. Each department (Node) is a connected compartment, and it holds people. If we need to add or delete a node, we can add in the beginning, the middle, or the end. If we want to see what is in the compartments, we must traverse through each one sequentially. Each element or Node has two parts: data and reference to the next Node. A linked list memory is not contagious; therefore, it is essential to use the link pointer of the head or the tail. The best way to learn how to use data structures it is important to write code.

## Purpose

A linked list is helpful in video games with more than one player. Once everyone has a turn, they have the option to start back at the first player until a winner is declared. A double-linked is incorporated on an iPhone music playlist, and we may play one song. We could play the previous song or the next song if we wanted to.

## Types

|     Term    |     Definition    |
|---|---|
|     Single Linked List    |     each Node stores the value and points to the next Node. It does not have any pointer to the previous Node. Each Node has two parts. The first part is the value, and the second part is the pointer or reference. The last Node is always null. The first Node points to the second Node. Flexible to add and remove nodes at run time. It cannot go back to the first Node.     |
|     Double Linked List    |     A double-linked list Resembles a single linked list. A double-linked list has two pointers from each Node and a value. It references the previous Node, and it references the next Node. Traverse backward and forward.     |
|     Circular Singly Linked List     |     Same as a single linked list, except the last node of the list stores a pointer/ reference to the first Node. The head has a physical location stored in the tail or last Node. If we traverse through the linked list, we have an option to visit the first Node. A circular, singly linked list creates a circle.     |
|     Circular Double Linked List    |     It is the same as a circular single-linked list, except it is accessible to traverse forward and backward. Loop indefinitely.     |

### Linked List vs. Arrays

A linked list is a data structure, and an array is not a data structure. Arrays and linked lists technically can do the same such as insertion, addition, and removal. The main difference between a linked list and an array is that a linked list is that each element in a linked list is independent of the other. In arrays, the data elements are not separate objects, so we cannot delete a cell, we can delete the value of the cell, but the cell will remain in memory. Unlike arrays, a linked list is efficient because we do not have to change each index when we insert and remove it. Arrays are great for finding items, but linked lists are better at insertions and removals.

## Structure

- A linked list has a construct

-
-

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
|     Append    |     Add a new node to the end of the list     |
|     Pop    |     remove last item from the end of the linked list     |
|     Prepend   |    Add a new node to the beginning of the linked list     |

## Operations

|     Term    |     Definition    |
|---|---|
|     Insert    |     Add a node to any location, beginning, middle, end    |
|     Traversal    |     Traverse all of the nodes from beginning to end.    |
|     Searching    |     Search the value of an element    |
|     deletion    |     Remove a node from the list.         |
|     Sort    |     Sort the Node of the linked list.    |

## Examples

### Linked list

Initialize a linked list
    - Initialize a class inked list(parameter of self)
    - Initialize/ initialize head and tail
    - Initialize a node
    - Initialize a pointer - this Initializes a link between the first Node and head.
    - Time Complexity O(1)

Initialize a class for nodes
    - initialize class Node
    - Set value and next
    - Time Complexity O(1)

```Python
    # Initialize a node class instead of adding a new node each time
    # each time we need a new Node.

    class Node 
        # Initialize a constructor with the parameter value and next. 
        def __init__(self, value)
            self.value = value 
            self.next = None
    
    # Initialize a linked list 
    
    class LinkedList:
        # method inside of a class
        # Initialize a constructor pass self and a value 
        def __init__(self, value):
            #Initialize a new Node call Node class pass value to it
            newNode = Node(value)
            # Initialize a head to point to newNode
            self.head = newNode
            # Initialize a tail to point to newNode
            self.tail = newNode
            # Initialize length to track and start at 1
            self.length = 1 
        
        # we need to print our list for testing purposes
        def print_list(self)
            while temp is not None:
                print(temp.value)
                temp = temp.next
# Testing
    # create first node
    linkedList = LinkedList(4)
    # print linked list
    print(linkedList.head.value)

```

### Example Initialize Insertion

```python
# Initialize method to add to the end or beginning of the list

        def append(self, value):
            #Initialize a Node and pass value
            newNode = Node(value)
            # Determine if head is empty
            # if empty set to head to None creating a pointer
            if self.head is None:
                self.head = newNode
                self.tail = newNode
            # otherwise do these steps 
            else:
                self.tail.next = newNode
            # move tail over one by Increase the length of the list by 1
            self.length += 1 
            # Return true not necessary 
            return True

        # initialize prepend method to add to the start of the linked list
        def prepend(self, value):
            #Initialize a Node and pass value
            newNode = Node(value)
            # Determine if head is empty
            # if empty set to head to None creating a pointer
            if self.length == 0;
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head = newNode
            self.length += 1
            return True
        
        def insert(self, pointer, value):
            # if we have an pointer out of range
            if pointer < 0 or pointer self.length:
                return False
            # if we are adding it to beginning
            if pointer == 0;
                # call prepend method 
                return self.prepend(value)
            # adding it to the end 
            if pointer == self.length:
                return self.append(value)
            # add in the middle 
            #Initialize a new node call Node and pass value
            newNode = Node(value)
            # Initialize temp variable call get method and 
            #  minus 1 to have it point to the correct node
            temp = self.get(pointer -1)
            # Set the next node on the new Node to the temp.next
            newNode.next = temp.next
            # set the temp.next node to the the new node add to the list
            temp.next = newNode
            # increment the link by one 
            self.length += 1
            return True
            
        

# Testing
    # create first node
    linkedList = LinkedList(4)
    # print linked list
    print(linkedList.head.value)
    # append linked list
    linkedList.append(2)
    # append list 
    listed.List.append(3)
    # print linked list
    linkedList.print()
    # prepend 
    linkedList.prepend(1)
    # print linked list
    linkedList.print() 
    # insert Method 
    linkedList = LinkedList(0)
    linkedList.append(2)
    linkedList.insert(1,1)
    linkedList.print_list()   
```

### Example Initialize Deletion

```python
        # Initialize the pop method to delete from the end
        def pop(self):
            # check if length of list is empty
            if self.length == 0:
                # return None 
                return None
            # Initialize temp and set to head
            temp = self.head
            # initialize previous and set to head
            previous = self.head
            # Loop through or traverse through linked list using the value of temp.next
            while(temp.next): # while true
                # point to the temp node
                previous = temp
                # set temp to temp.next to move temp over to the next node
                temp = temp.next
            # set tail to previous node
            self.tail = previous
            # set tail next node to none that will remove the node
            self.tail.next = None
            # decrement the link by 1 
            self.length -= 1
            # If we only have one node and remove it set head and tail to None
            if self.length == 0:
                self.head = None
                self.tail = None
            # to test return temp.value
            return temp
         # Initialize the pop first method to delete from the end

        def popFirst(self):
            # check if length of list is empty
            if self.length == 0:
                # return None 
                return None
            # Initialize temp and set to head
            temp = self.head
            # set self.head to self head next
            self.head = self.head.next
            # decrement the link by 1 
            self.length -= 1
            # set tail to none
            if self.length == 0:
                self.tail = None
            return temp

        def remove (self, pointer):
            # dealing with an invalid range
            if pointer < 0 or pointer >= self.length:
                return None
            # if we are removing node from the beginning
            if pointer == 0;
                # call pop first method to remove from the beginning
                return self.pop_first()
            # removing from the end 
            if pointer == self.length - 1:
                # call pop method to remove from the end
                return self.pop()
            # remove from the middle 
            # set previous 
            previous = self.get(index -1)
            # set temp to previous next 
            temp = previous.next
            # remove link by setting to none
            temp.next = None
            # minus the node from the length count
            self.length -= 1
            # return temp.value to code 
            return temp
            

# Testing
    # (2) Items - Returns 2 Node
    print(linkedList.pop())
    # (1) Item -  Returns 1 Node
    print(linkedList.pop())
    # (0) Items - Returns None
    print(linkedList.pop())
    # (2) Items - Returns 2 Node
    print(linkedList.pop_first())
    # (1) Item -  Returns 1 Node
    print(linkedList.pop_first())
    # (0) Items - Returns None
    print(linkedList.pop_first())   
    # test remove

    linkedList = LinkedList(11)
    linkedList.append(3)
    linkedList.append(23)
    linkedList.append(7)
    print(linkedList.remove(2), '\n')
    linkedList.print_list()
```

### Example Initialize Search

```python

    def get(self, pointer):
        # test to see if pointer is valid 
        if pointer < 0 or pointer >= self.length:
            return None
        temp = self.head
         # put an underscore because we are not going to use the variable 
        for _ in range(pointer):
            temp = temp.next 
        return temp
    
    # to set a value after we get it 
    def set_value(self, pointer, value):
        # similar to get Initialize temp and call get with parameter pointer
        temp = self.get(pointer)
        # check to see if list has a node or if returns None 
        if temp:
            temp.value = value
            return True
        return False 

# testing 
linkedList = LinkedList(0)
linkedList.append(1)
linkedList.append(2)
linkedList.append(3)

print(linkedList.get(2))

# test set 
linkedList = LinkedList(11)
linkedList.append(3)
linkedList.append(23)
linkedList.append(7)

linkedList.set_value(1,4)

linkedList.print_list()

```

### Traverse 

```python
    def reverse (self, value)
        # initialize temp 
        temp = self.head
        # set head to tail
        self.head = self.tail 
        # set tail to temp 
        self.tail = temp
        
        # initialize after 
        after = temp.next
        # initialize before     
        before = None 
        for _ in range(self.length):
            # four steps
            # this has to happen first
            after = temp.next 
            # flips the link 
            temp.next = before 
            # create link where the link was broken 
            before = temp 
            # Moves temp over ore creates a link 
            temp = after 
# Testing 
linkedList = LinkedList(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.reverse()
linkedList.print_list()
    
```

## Problem

### Before Coding

- List test cases and their answers
- Consider the problems.
- Evaluate your code against all test cases
- Do not Rush to Code
- Make code simple and short code
- Sketch everything on paper first
- Draw out sketches
- Pick out clear names
- Reuse code
- In algorithm make sure you handle all run time errors in logic
- Verifying against null nodes
- Data integrity
  - What is your data?  Head, Tail, length
    - Head and tail should be null or none if empty
    - Length must be really the length of the items
  - Write a function that verifies a linked list is correct
    - if self.length == 0; assert self.head is none same for tail then return
    - check assert self.tail.next is none
    - If self.length is equal to 1 assert head to equal tail
    - if self.length is equal to 2 assert head.next to equal tail

### Solve

Our music on our iPod will not play the previous song.

You can check your code with the solution here: [Solution](2-topic-solution.py)

[Back to Welcome Page](0-welcome.md)

Works Cited
<https://www.123rf.com/photo_128160367_stock-vector-passenger-tram-train-realistic-mockup-with-side-view-of-three-metropolitan-trains-with-various-color.html>

<https://www.dreamstime.com/train-tram-subway-wagons-side-view-metro-locomotive-rails-isolated-modern-commuter-city-transport-railway-vehicle-modes-image226814646>
<https://www.programiz.com/dsa/linked-list-operations>
