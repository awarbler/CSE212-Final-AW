# Queues
<!-- This content will not appear in the rendered Markdown -->
A Queue is a type of data structure that is a collection of entities. It follows a linear operation. For example, a queue data structure follows the process of first-in, first-out, or FIFO. The first data is stored first, and data will be the first to get deleted. For example, renew a driver's license, go to the Department of motor vehicles; take a number; if the line is empty, the number will be first or put at the end of the line, the first number goes first, and the last number is the last to be served.

## Purpose

In software engineering, we will need to use queues. We need to use a queue data structure to program an application that utilizes FIFO. The first application is a point of sale standing in a line at the grocery store. The first customer in line must be processed in the order they arrived. The second is a shared printer at home. The printer will print the first document sent to the printer, and the other documents will wait until the first is printed. The third is a call center. Queues are used in everyday transactions such as grocery store lines, point of sales, printer queues, and call centers. Queues are used to manage a group of objects.

## Types

There are four types of queues Simple Queue, Circular Queues, Priority Queues, and Double Queues. These different types of queues use python lists and linked lists. Table 1.1 below explains the differences between the four queues.[^1]

|     Type    |     Description     |
|:---|:---|
|     Circular Queue    |     The last element points to the first element making a circle. A circular queue has a capacity—a circular queue, otherwise known as a linked list.    |
|     Double Queue    |     Insert and remove may occur from the front or last. It may be set to have a capacity.   |
|     Priority Queue    |     Each element is associated with a priority and served by its importance. It may be set to have a capacity.   |
|     Simple Queue    |     Insert in the rear removal in the front. It may be set to have a capacity.    |

Queues may also use python lists or linked lists. Using a linked list will work best if we set a queue with a capacity that is a circular queue. A python list without a set capacity is a single query; it is a slow process. This tutorial will use a simple queue using a python list FIFO.

## Queue Terminology

Table 1.2 explains the basic definitions for data structure and queues.

|     Term    |     Definition    |
|---|---|
|     back    |     The location an enqueue takes place. All enqueues occur at the end of the last item in the queue.      |
|     Big O notation    |     Big O notation is an algorithm calculates run-time complexities. Here are the most used complexities.    |
|     front    |     The front is the location where a dequeue takes place. All dequeues occur at the beginning of the first item in the queue.     |
|     O(1)    |     Constant - Accessing a specific element or location    |
|     O(N)    |     Linear Loop through an element or grow in direction, the larger the input, the greater amount of time it takes to traverse through every item    |
|     O(LogN)    |     Logarithmic -Find an element proportionally to the logarithm of the input size. The function does not pass through or search every item in the queue. Tend to be used in binary search, searching uses compare functions. For each step, we tend to divide by two; the total time is divided by 2    |
|     O(n^2)    |     Quadratic -Looking at every index more than once, primarily used in nesting loops, searching over information more than one time     |
|     O(2^n)     |     Exponential -Double recursion in Fibonacci    |

## Operations

Queue modules implement multiproduct, multicomputer queues. Table 2 shows the main methods used to implement a queue and an example.

|     Method    |     Description    |     Example    |     Notation    |
|---|---|---|---|
|     Delete()    |     The delete function allows us to delete the entire queue    |     queue.isEmpty()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Dequeue()    |     Deletes data from a queue. If there is only one element, the list will be empty. Deletes from the front of the queue.     |     queue.Dequeue() or value = queue.pop(0)    |     O(1) – order of 1, remains constant, access a specific element    |
|     Enqueue()    |     Inserts data into a queue. It cannot insert data elements in the middle of a python list. Instead, each element is behind one another added at the back of the queue.    |     queue.Enqueue(25) or     queue.append(value)    |     O(1) – order of 1, remains constant, access a specific element    |
|     Front()    |     Returns the front item from the queue    |     queue.Front()    |     O(1) – order of 1, remains constant, access a specific element    |
|     isEmpty()    |     Checks if there is an element in a queue or if it is empty. It will return either true or false.     |     queue.isEmpty()    |     O(1) – order of 1, remains constant, access a specific element    |
|     isFull()    |     These are used in circular queues. If a queue is set, isFull will check if the capacity is full. If it isFull(), we cannot add it to the queue     |     queue.isFull()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Rear()    |     Returns the back item from the queue.    |     queue.Rear()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Size()    |     Checks the size of the queue    |     len(queue) == size    |     O(1) – order of 1, remains constant, access a specific element    |

## Example Queue without Capacity

To use queue data structure, we will need to set up a class called queue and methods. This example uses a python list with no capacity.

Here are the standard queue operations:

1. Initialize a Queue

    - Initialize a class that calls parameter self
    - Initialize an empty python list
    - It is set to zero.
    - Insert as many elements that are needed
    - Time Complexity O(1)

        ``` python
        class Queue:
            def __init__(self):
                self.items = []
        ```

2. Let's Initialize a method that will help us run and print our test.
    - Initialize a method that calls parameter self
    - Print out the queue correctly
    - Time Complexity O(1)

    ```python
        def __str__(self):
            values = [str(x) for x in self.items]
            return ' '.join(values)
    ```

3. Initialize the isEmpty Method
    - Initialize a method that calls parameter self
    - The isEmpty method is used inside other methods to check elements.
    - In some cases, if the queue isEmpty there is no point in running the other methods.
    - Time Complexity O(1) checking one item

     ``` python
        def isEmpty(self):
            if self.items == []:
                return True
            else:
                return False
    ```

4. Initialize an enqueue method
    - Initialize a method that calls parameter self
    - The element will be assigned a location
    - The second element will be assigned a location after the first element in the queue.
    - Time Complexity O(n)

    ``` python
        def enqueue(self, value):
            self.items.append(value)
            return "The element is inserted at the end of Queue"
    ```

5. Initialize a dequeue method
    - Dequeue is used instead of the remove function.
    - Call the isEmpty function
    - Dequeue will return the first element and will be removed.
    - It is best to add in an error if the queue is empty.
    - Time Complexity O(n)

    ``` python
        def dequeue(self):
            if self.isEmpty():
                return "The is not any element in the Queue"
            else:
                return self.items.pop(0)
    ```

6. Initialize a peek method
    - It is similar to the dequeue, except it will not be updated.
    - We are not removing the element.
    - Every time, the same element will be returned.
    - Time Complexity O(1)

    ```python
        def peek(self):
            if self.isEmpty():
                return "The is not any element in the Queue"
            else:
                return self.items[0]
    ```

7. Initialize the delete method
    - The delete method will delete the entire queue.
    - This will set the queue to none.
    - Time Complexity O(1)

    ```python
        def delete(self):
            self.items = None
    '''

8. Test the queue
    - Check if the Method works
    - Initialize a variable
    - Print the value of the queue
    - The method will return true, which means our queue is empty.
    - Call all of our methods as a test.
    - It is best to print out the queue for testing.

    ```python
        testQueue = Queue()
        # call isEmpty method
        print(testQueue.isEmpty())
        # call enqueue method
        testQueue.enqueue(1)
        testQueue.enqueue(3)
        testQueue.enqueue(4)
        testQueue.enqueue(5)
        # call dequeue method 
        print(testQueue.dequeue())
        # call print function to see if item was dequeue
        print(testQueue)
        
    ```

## Example Queue with Capacity

Using a python list with a set capacity is similar to creating a python list without a set capacity. Set a class called queue and the same methods.

1. Initialize a Circular Queue
    - Initialize a blank list
    - Set a fixed size max to 6
    - Initialize a start and set it to - 1
    - Initialize top variables set to -1

    ```python
    class Queue:
        def __init__(self, maxSize):
            self.items = maxSize * [None]
            self.maxSize = maxSize
            self.start = -1
            self.top = -1
    ```

2. Initialize a method that will help us run and print our test.
    - Print out the queue correctly
    - Time Complexity O(1)

    ```python
        def __str__(self):
            values = [str(x) for x in self.items]
            return ' '.join(values)
    ```

3. Initialize isFull Method
    - Check if the queue is full
    - Add a condition if the list is before the start; no blank list
    - Add a condition if the start is zero, that means it is full
    - add one since the list starts at zero
    - Return true otherwise, false
    - Time complexity is O(1)

    ```python
        def isFull(self):
            if self.top + 1 == self.start:
                return True
            elif self.start == 0 and self.top + 1 == self.maxSize:
                return True
            else:
                return False
    ```

4. Initialize isEmpty Method
    - add a condition to check if it is negative 1
    - Return True
    - Returns False
    - Time complexity O(1)

    ```python

        def isEmpty(self):
            if self.top == -1:
                return True
            else:
                return False
    ```

5. Initialize enqueue Method
    - Accept parameter of self and value
    - Add a condition to call isFull()
    - If full, we cannot insert element
    - If not, Continue to insert the element into the queue
    - Add a condition if top plus one equals maxSize
    - Our top points to the last element
    - Update to zero
    - Otherwise, add one to the top to point to the next element
    - If we are adding the first element to an empty queue, we need to update it to zero because the index of the first element is zero
    - if self starts equals minus one, it means we are inserting the first element
    - Set start to zero and add the element to the list
    - Update the value of top
    - Return saying the element has been inserted
    - Time complexity is O(1)

    ```python

        def enqueue(self, value):
            if self.isFull():
            return "The queue is full"
            else:
                if self.top + 1 == self.maxSize:
                    self.top = 0
                else:
                    self.top += 1
                    if self.start == -1:
                        self.start = 0
                self.items[self.top] = value
                return "The element is inserted at the end of Queue"
        
    ```

6. Initialize the dequeue method
    - dequeue method will call parameter self
    - Call isEmpty Method
    - If true, return the message
    - add a condition with a temp variable return items equals self. start
    - Add a condition to check if start is equal to self-start
    - Set start and top property to minus one
    - If this is the only element in the queue.
    - Update the self start to minus one and self top to minus one because it is the last element in the queue
    - The queue will be empty
    - In else elif we need to point to the beginning of the list
    - Set the self-start plus one equals self maxSize
    - In the else condition, increase the self start every time by one
    - At the end, set self item start to none
    - Return the first element
    - Time complexity o(1)

    ```python
        def dequeue(self):
            if self.isEmpty():
                    return "There is not any element in the Queue"
                else:
                    firstElement = self.items[self.start]
                    start = self.start
                    if self.start == self.top:
                        self.start = -1
                        self.top = -1
                    elif self.start + 1 == self.maxSize:
                        self.start = 0
                    else:
                        self.start += 1
                    self.items[start] = None
                    return firstElement

    ```

7. Initialize peek Method
    - start property points to the first element
    -

    ```python
        def peek(self):
            if self.isEmpty():
                return "There is not any element in the Queue"
            else:
                return self.items[self.start]

    ```

8. Delete Method
    - Setting to none

    ```python
        def delete(self):
            self.items = self.maxSize * [None]
            self.top = -1
            self.start = -1

    ```

9. Test Code
    - write code to test methods

    ```python
    # assign tQueue
    tQueue = Queue(3)
    # call isFull
    print(tQueue.isFull())
    # call isEmpty
    print(tQueue.isEmpty())
    # add data
    tQueue.enqueue(1)
    tQueue.enqueue(2)
    tQueue.enqueue(3)
    # print queue to see if enqueued
    print(tQueue)
    # call dequeue method
    print(tQueue.dequeue())
    
    
    ```

## Problem

The Bishops storehouse holds canned and bagged food. The food storage works strictly on a "first-in, first-out" basis. People must use the food based on the arrival of all food at the storehouse, or they can select whether they want bagged food or canned food and will receive the oldest food of that type. However, they cannot choose which specific food they would like. Initialize a data structure to maintain this system and implement operations such as enqueue, dequeueAny, and dequeueBagged dequeueCanned.


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
- Verifying against null nodes
- Data integrity 

You can check your code with the solution here: [Solution](1-topic-solution.py)

[Back to Welcome Page](0-welcome.md)

### Footnotes

[^1]: Queues (https://www.programiz.com/dsa/types-of-queue )

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].  

You can also use words to fit your writing style more closely[^note].

1: My reference.
[^2]: Every new line should be prefixed with two spaces.  
  This allows you to have a footnote with multiple lines.
[^note]:
    Named footnotes will still render with numbers instead of the text, allowing easier identification and linking.  
    This footnote also has been made with a different syntax using four spaces for new lines.



