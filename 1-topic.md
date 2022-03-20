# Queues

A Queue is a type of data structure that is a collection of entities. It follows a linear operation. For example, a queue data structure follows the operation of first-in, first-out, or FIFO. The first data is stored first, and data will be the first to get deleted. For example, renew a driver's license, go to the Department of motor vehicles; take a number, if the line is empty, the number will be first or put at the end of the line, the first number goes first, and the last number is the last to be served.

## Purpose

In software engineering, we will need to use queues. We need to use a queue data structure to program an application that utilizes FIFO. The first application is a point of sale standing in a line at the grocery store. The first customer in line must be processed in the order they arrived. The second is a shared printer at home. The printer will print the first document sent to the printer, and the other documents will wait until the first is printed. The third is a call center. Queues are used in everyday transactions such as grocery store lines, point of sales, printer queues, and call centers. Queues are used to manage a group of objects.

## Types

There are four types of queues Simple Queue, Circular Queues, Priority Queues, and Double Queues. These different types of queues use python lists and linked lists. Table 1.1 below explains the differences between the four queues.

|     Type    |     Description     |
|:---|:---|
|     Simple Queue    |     Insert in the rear removal in the front. May be set to have a capacity.    |
|     Circular Queue    |     The last element points to the first element making a circle. A circular queue has a capacity—a circular queue, otherwise known as a linked list.    |
|     Priority Queue    |     Each element is associated with a priority and served by its priority.May be set to have a capacity.   |
|     Double Queue    |     Insert and remove may occur from either the front or last. May be set to have a capacity.   |

Queues may also use python lists or linked lists. Using a linked list will work best if we set a queue with a capacity that is a circular queue. A python list without a set capacity is a single query it is a really slow process. This tutorial will use a simple queue using a python list FIFO.

## Queue Terminology

Table 1.2 explains the basic definitions for data structure and queues.

|     Term    |     Definition    |
|---|---|
|     back    |     The location an enqueue takes place. All enqueues occur at the end of the last item in the queue.      |
|     front    |     The front is the location where a dequeue takes place. All dequeues occur at the beginning of the first item in the queue.     |
|     Big O notation    |     Big O notation is an algorithm that calculates run-time complexities. Here are the most used complexities.    |
|     O(1)    |     Constant - Accessing a specific element or location    |
|     O(N)    |     Linear Loop through an element or grow in direction, the larger the input, the greater amount of time it takes, traverse through every   item    |
|     O(LogN)    |     Logarithmic -Find an element proportionally to the logarithm of the input size. The function does not pass through or search every item in the queue. Tend to be used in binary search, searching uses compare functions. Each step we tend to divide by two the total time is divided by 2    |
|     O(n^2)    |     Quadratic -Looking at every index more than once, primarily used in nesting loops, searching over information more than one time     |
|     O(2^n)     |     Exponential -Double recursion in Fibonacci    |

## Operations

Queue modules implement multiproduct, multicomputer queues. In table 2, are the main methods used in implementing a queue and an example.

|     Method    |     Description    |     Example    |     Notation    |
|---|---|---|---|
|     Enqueue()    |     Inserts data into a queue. It cannot insert data elements in the middle of a python list. Instead, each element is behind one another added at the back of the queue.    |     queue.Enqueue(25) or     queue.append(value)    |     O(1) – order of 1, remains constant, access a specific element    |
|     Dequeue()    |     Deletes data from a queue. If there is only one element, the list will be empty. Deletes from the front of the queue.     |     queue.Dequeue() or value = queue.pop(0)    |     O(1) – order of 1, remains constant, access a specific element    |
|     isEmpty()    |     Checks if there is an element in a queue or if it is empty. It will return either true or false.     |     queue.isEmpty()    |     O(1) – order of 1, remains constant, access a specific element    |
|     isFull()    |     These are used in circular queues. If a queue is set, isFull will check if the capacity is full. If it isFull(), we cannot add it to the queue     |     queue.isFull()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Front()    |     Returns the front item from the queue    |     queue.Front()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Rear()    |     Returns the back item from the queue.    |     queue.Rear()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Delete()    |     The delete function allows us to delete the entire queue    |     queue.isEmpy()    |     O(1) – order of 1, remains constant, access a specific element    |
|     Size()    |     Checks the size of the queue    |     len(queue) == size    |     O(1) – order of 1, remains constant, access a specific element    |

## Example Methods

To use queue data structure we will need to set up a class called queue and methods. We are going to use a python list and it is important to set the capacity of a list to make the list time effecient.

Here are the standard queue operations:

1. Create a Queue
    - Initialize an empty python list
    - It is set to zero.
    - Insert as many elements that is needed

        ``` python
        class Queue:
            def __init__(self):
                self.items = []
        ```

2. Let's create a method that will help us run and print our test.

    ```python
        def __str__(self):
            values = [str(x) for x in self.items]
            return ' '.join(values)
    ```

3. Create the isEmpty method
    - The isEmpty method is used inside other methods to check elements.
    - In some cases, if the queue isEmpty there is no point in running the other methods.

     ``` python
        def isEmpty(self):
            if self.items == []:
                return True
            else:
                return False
    ```

4. Create an enqueue method
    - The element will be assigned a location
    - The second element will be assigned a location after the first element in the queue.

    ``` python
        def enqueue(self, value):
            self.items.append(value)
            return "The element is inserted at the end of Queue"
    ```

5. Create a dequeue method
    - Dequeue is used instead of the remove function.
    - Dequeue will return the first element and will be removed.
    - It is best to add in an error if the queue is empty.

    ``` python
        def dequeue(self):
            if self.isEmpty():
                return "The is not any element in the Queue"
            else:
                return self.items.pop(0)
    ```

6. Create a peek method
    - It is similar to the dequeue, except it will not be updated.
    - We are not removing the element.
    - Every time the same element will be returned.

    ```python
        def peek(self):
            if self.isEmpty():
                return "The is not any element in the Queue"
            else:
                return self.items[0]
    ```

7. Create delete method
    - The delete method will delete the entire queue.
    - This will set the queue to none.

    ```python
        def delete(self):
            self.items = None
    '''

You can check your code with the solution here: [Solution](1-topic-solution.py)

[Back to Welcome Page](0-welcome.md)
