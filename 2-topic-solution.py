class Node:

        def __init__(self, value):
            self.value = value 
            self.next = None

class Playlist():
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1 

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1 
        # Return true not necessary 
        return True

    def pop(self):

        if self.length == 0:
            return None
        temp = self.head
        previous = self.head
        while(temp.next): 
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
            # return temp use temp.value for testing
        return temp.value

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        # return temp use temp.value for testing
        return temp.value

    def get(self, pointer):
        if pointer < 0 or pointer >= self.length:
            return None
        temp = self.head
        for _ in range(pointer):
            temp = temp.next
        return temp

    def insert(self, pointer, value):
        if pointer < 0 or pointer > self.length:
            return False
        if pointer == 0:
            return self.prepend(value)
        if pointer == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(pointer -1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True   

    def remove (self, pointer):
        if pointer < 0 or pointer >= self.length:
            return None
        if pointer == 0:
            return self.pop_first()
        if pointer == self.length - 1:
            return self.pop()
        previous = self.get(pointer -1)
        temp = previous.next
        temp.next = None
        self.length -= 1
        # return temp use temp.value for testing
        return temp.value

    def setValue(self, pointer, value):
        temp = self.get(pointer)
        if temp:
            temp.value = value
            return True
        return False

#Test
print("New linked list")
song = Playlist(2)
# print linked list
print(song.head.value)
# append list 
song.append(3)
print("added append and now printing list")
song.print()
# prepend 
song.prepend(1)
print("added prepend and now printing list")
song.print()
# append list 
song.append(3)
print("added append and now printing list")
song.print()
# Returns 2 Node
print(song.pop())
print("pop and now printing list")
song.print()
#Returns None
print(song.pop())
print("pop and now printing list")
song.print()
# (Returns 2 Node
print(song.popFirst())
print("pop first and now printing list")
song.print() 
# insert Method 
song.insert(1,1)
print("added insert and now printing list")
song.print() 
song.append(3)
print("added append and now printing list")
song.print() 
song.append(23)
print("added append and now printing list")
song.print() 
song.append(7)
print("added append and now printing list")
song.print() 
print(song.remove(2))
print("added remove and now printing list")
song.print()
song.setValue(1,4)
print("added setValueand now printing list")


        




 

# # testing 
# song = LinkedList(0)
# song.append(1)
# song.append(2)
# song.append(3)

# print(song.get(2))

# # test set 
# song = LinkedList(11)
# song.append(3)
# song.append(23)
# song.append(7)

# song.set_value(1,4)

# song.print_list()



# ### Traverse 

# ```python
#     def reverse (self, value)
#         # initialize temp 
#         temp = self.head
#         # set head to tail
#         self.head = self.tail 
#         # set tail to temp 
#         self.tail = temp
        
#         # initialize after 
#         after = temp.next
#         # initialize before     
#         before = None 
#         for _ in range(self.length):
#             # four steps
#             # this has to happen first
#             after = temp.next 
#             # flips the link 
#             temp.next = before 
#             # create link where the link was broken 
#             before = temp 
#             # Moves temp over ore creates a link 
#             temp = after 
# # Testing 
# song = LinkedList(1)
# song.append(2)
# song.append(3)
# song.append(4)
# song.reverse()
# song.print_list()
    
###############################



# # Testing


 
