## Problem

#The Bishops storehouse hold canned and bagged food.  
# The food storage works strictly on "first in, first out" basis. 
# People must use the food based on  arrival of all food at the storehouse, 
# or they can select whether they want bagged food or canned food and will 
# receive the oldest food of that type. They cannot select which specific 
# food they would like. Initialize a data structure to maintain this system 
# and implement the operation such as enqueue, dequeueAny, dequeueBagged, dequeueCanned.

# Create a data structure to maintain the system


class BishopStore():
    """
    Implement a queue 
    """
    
    def __init__(self) :
        """
        Create empty queues to hold the data
        """
        self.cannedFood = []
        self.baggedFood = []
    
    def enqueue(self, food, type):
        """
        Add an item to the queue adding value and type to the parameter
        """
        if type == 'canned':
            self.cannedFood.append(food)
        else:
            self.baggedFood.append(food)
    
    def dequeueBagged(self):
        """
        Remove bagged food from the queue and check if empty 
        """
        if len(self.baggedFood)== 0:
            return None
        else:
            bagged = self.baggedFood.pop(0)
        return bagged
    def dequeueCanned(self):
        """
        remove canned food from the queue and check if empty 
        """
        if len(self.cannedFood)== 0:
            return None
        else:
            canned = self.cannedFood.pop(0)
        return canned
        
    def dequeueAny(self):
        if len(self.cannedFood) == 0:
            anyFood = self.cannedFood.pop(0)
        else:
            anyFood= self.baggedFood.pop(0)
        return anyFood

    