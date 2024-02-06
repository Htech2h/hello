class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    #the add at front creates a head node which point to the next node
    def add_at_front(self, data):
        self.head = Node(data, self.head)

    #the if block code is designed to add at the end of the linked list even if it's empty
    def add_at_end(self, data):
        if not self.head: #this means if there is no head or linkedlist is empty(no node assigned to the head)
            self.head = Node(data, None) #then creates a node which doesnt point to nothing meaning it will be the last node
            return #stops the method, but the below code runs if this is false
        curr = self.head #but if head node exist curr takes it
        while curr.next: #if curr is followed 
            curr = curr.next #then curr always takes the node that follow
        curr.next = Node(data, None) #then turns the none to the data its caring at point it to none making it the last

    def get_last_node(self): # get the right most node
        n = self.head #similar to curr (take the head node if it exist)
        while(n.next != None):#if the head is followed by other nodes
            n = n.next #take of the right most node
        return n.data #this returns the data of the right most node

    def is_empty(self): #checks if there is a head node. if there is head it returns false
        return self.head == None #and true if head is empty

    def print_list(self):
        n = self.head # take the head
        while n != None: #the loop stops after printing the last node as it points to none
            print(n.data, end = " => ") # prints the data followed by =>
            n = n.next # n takes node of next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())