# Queues

A Queue is a type of data structure that is a collection of entities. It follows a linear operation. For example, a queue data structure follows the operation of first-in, first-out, or FIFO. The first data is stored first, and data will be the first to get deleted. For example, renew a driver's license, go to the Department of motor vehicles; take a number, if the line is empty, the number will be first or put at the end of the line, the first number goes first, and the last number is the last to be served. Queues are used in everyday transactions such as grocery store lines, point of sales, printer queues, and call centers.

## Types

There are four types of queues Simple Queue, Circular Queues, Priority Queues, and Double Queues. Table 1.1 below explains the differences between the four queues:

|     Type    |     Description     |
|:---|:---|
|     Simple Queue    |     Insert in the rear removal in the front. May be set to have a capacity.    |
|     Circular Queue    |     The last element points to the first element making a circle. A circular queue has a capacity—a circular queue, otherwise known as a linked list.    |
|     Priority Queue    |     Each element is associated with a priority and served by its priority.May be set to have a capacity.   |
|     Double Queue    |     Insert and remove may occur from either the front or last. May be set to have a capacity.   |

This tutorial will focus on using a simple queue using a python list FIFO.

## Queue Terminology
|     Term    |     Definition    |
|---|---|
|     back    |     The location an enqueue takes place. All enqueues occur at   the end of the last item in the queue.      |
|     front    |     The front is the location where a dequeue takes place. All   dequeues occur at the beginning of the first item in the queue.     |
|     Big O notation    |     Big O notation is an algorithm that calculates run-time complexities.   Here are the most used complexities.    |
|     O(1)    |     Constant - Accessing a specific element or location    |
|     O(N)    |     Linear Loop through an element or grow in direction, the   larger the input, the greater amount of time it takes, traverse through every   item    |
|     O(LogN)    |     Logarithmic -Find an element proportionally to the   logarithm of the input size. The function does not pass through or search every   item in the queue. Tend to be used in binary search, searching uses compare functions.   Each step we tend to divide by two the total time is divided by 2    |
|     O(n^2)    |     Quadratic -Looking at every index more than once, primarily   used in nesting loops, searching over information more than one time     |
|     O(2^n)     |     Exponential -Double recursion in Fibonacci    |

## Implementing Queues

Queue modules implement multiproduct, multicomputer queues. In table 2, there are the main methods used in implementing a queue and an example.

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

Software would be very boring if we didn't have the ability to make choices.  Imagine you had a game app on your phone that didn't allow you to make any choices:

- You wouldn't be able to set an avatar if you select one when the game starts
- You wouldn't be able to move if you swipe left or right
- You wouldn't be able to change to a new level if you completed all the tasks
- You wouldn't be able to start the game over if you lose
- You wouldn't be able to fire your weapon if you pull the trigger (and likewise, neither would your enemies)
- In reality, the game would always run the exact same way regardless of what you tried to do

A conditional in Python is written using the `if`statement.  In the example below, a message is displayed if the temperature is below freezing (using units of Fahrenheit):

```
  if temp <= 32.0:
         print("Watch for ice!")

```

In Python, we use the colon (`:`) to indicate the beginning of a block of code.  In this case, the block of code that displays the message will only occur the the condition is True.  The condition `temp <= 32.0` is called a boolean expression.  A boolean expression will also result in a True or a False.  If the boolean expression is True, then code in the block will run.

## Boolean Expressions

A boolean expressions will use one or more of the following boolean operators:

- `==`  :  Equal To (Don't confuse this with a single `=` sign which is used for assigning a value to a variable)
- `>` : Greater than
- `>=` : Greater than or equal too
- `<` : Less than
- `<=` : Less than or equal too
- `!=` : Not equal To

Here are some examples of Boolean Expressions:

```python
if name == "Bob":
 print("We found Bob!")
 
if pressure > 100:
 print("Danger! High Pressure Alert!")
 
if choice != "quit":
 print("Let's keep playing")
```

We can make compound boolean expressions by combining one or more boolean expressions together using these boolean operators:

- `and` : Test to see if both boolean expressions are True
- `or` : Test to see if at least one of the two boolean expression are True
- `not`: Test to see if a boolean expression is False (note this one only deals with one boolean expression)

We can make compound boolean expressions as complicated as they need to be.  We can use parentheses to help create the right scenarios.  Here are some examples:

```python
if temp > 50 and wind < 20:
 print("Lets go hiking!")
 
if pressume < 20 or (pressure < 30 and leak_detected == True):
 print("Someone quickly close the valve!")
 
# We can rewrite the previous example without the == because leak_detected
# is already a boolean.  Here is how we do that:

if pressure < 20 or (pressure < 30 and leak_detected):
 print("Someone quickly close the valve!")
 
if (not alive) and (points > 30) and (name != "Bob"):
 print("Since you did well (and you are not Bob), you get to play again!")
```

## Multiple Conditions

When we allow the software to make decisions, there might be more than one decision that should be made.  Specifying multiple conditions in python uses the `elif` and `else` keywords.  The `elif` keyword means "else if" and represents an additional condition.  The `else` keyword represents all other possible conditions.  Here is a complete example to consider:

```Python
if temp <= 32.0:
 print("Watch for ice!")
elif temp <= 50.0:
 print("Might want to bring a jacket!")
elif temp <= 80.0:
 print("What a beautiful day!")
else:
 print("Its warm out there ... look for some shade!")
```

When this code runs, if will first consider the `temp <= 32.0` condition.  If its True, then it will run the code within the block but then skip all the other conditions.  If the first condition was False, then it will consider the second condition `temp <= 50`.  Notice that in this second condition, we can assume that the temperature is already great than 32.0 because the first condition failed.  If none of the first 3 conditions result in a True (perhaps the temperature is balmy 90 degrees), then the `else` condition will result in True.  Notice that we never put a boolean condition next to the keyword `else`.

Sometimes programmers think they always need to put an `elif` and an `else` when they write an `if` statement.  This is not true.  You should think about all the scenarios you want to check for and use the `elif` and `else` as needed.  If we wrote the same code above  but without `elif` and `else`, we would have to write more complicated boolean expressions.  It is better to use `elif` and `else` to simplify the code and ensure the result we want.

## Example : Geometry Calculator

In the example below, we will write a simple Geometry Calculator.  Before we write the code, we should first think about what we want the software to do.  Writing a list of requirements is an important step in writing software.  The requirements can help us ensure that we using conditionals correctly.  

Geometry Calculator Requirements:

- Allow the user to select the shape they want to calculate the area for
- Ask the user for the size information of the shape they selected
- Ensure that size lengths are all valid (greater than zero)
- Display the results

```python
import math

print("Welcome to the Geometry Calculator")
print("Please select a shape:")
print("1) Square")
print("2) Triangle")
print("3) Circle")
choice = int(input("> "))  
if choice == 1:
    side = float(input("Side length of the square: "))
    if side > 0:
        area = side ** 2
        print("The area is {}".format(area))
    else:
        print("Invalid side length!")
elif choice == 2:
    base = float(input("Length of the triangle base: "))
    height = float(input("Length of the triangle height: "))
    if base > 0 and height > 0:
        area = 0.5 * base * height
        print("The area is {}".format(area))
    else:
        print("One of the lengths was invalid!")
elif choice == 3:
    radius = float(input("Raidus of the circle: "))
    if radius > 0:
        area = math.pi * radius * radius
        print("The area is {}".format(area))
    else:
        print("Invalid radius length!")
else:
    print("Invalid Menu Selection")
```

Note the use of `elif` to provide conditions for different choices and `else` for the special condition of an invalid choice.  Within each conditional block, different prompts, variables, expressions, and conditionals are used.

## Problem to Solve : Summer Camp Cost

Write a program that will determine the cost for a child to attend a summer camp based on various factors described below:

The base cost of attending summer camp is determined by the age of the child:

|   Age   |      Cost      |
| :-----: | :------------: |
| Under 8 | Can not attend |
|  8-10   |     $1000      |
|  11-12  |     $1500      |
|  13-16  |     $2000      |
| Over 16 | Can not attend |

The base cost is reduced based on the number of children (of any age) in the family and the family income:

| Family Income        | 1 Child in Family | 2 Children in Family | 3+ Children in Family |
| -------------------- | ----------------- | -------------------- | --------------------- |
| Under 25K per Year   | - 70%             | - 80%                | - 90%                 |
| Under 50K per Year   | - 40%             | - 50%                | - 60%                 |
| Under 75K per Year   | - 10%             | - 20%                | - 30%                 |
| 75K or More per Year | No Reduction      | No Reduction         | No Reduction          |

You can test your program with the following scenarios:

- Test 1: 10 year old, 2 children in the family, family income 45K per year will cost: $500 (50% off)
- Test 2: 14 year old, 3 children in the family, family income 70K per year will cost: $1400 (30% off)
- Test 3: 12 year old, 1 child in the family, family income 80K per year will cost: $1500 (0% off)
- Test 4: 18 year old, 3 children in the family, family income 23K per year will cost: N/A - They can't attend

You can check your code with the solution here: [Solution](1-topic-solution.py)

[Back to Welcome Page](0-welcome.md)
