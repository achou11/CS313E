# File: Circular.py
# Description: Simulation of hot potato game using concept of circular linked list.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320

# Date Created: 10/27/16
# Date Last Modified: 10/28/16

#create node class
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next           
    
    def setData(self, newData):
        self.data = newData
    
    def setNext(self, newNext):
        self.next = newNext


#create circular linked list class
class CircularList(object):
    
    def __init__(self):
        #create sentinel node
        sentinel = Node(None)
        self.head = sentinel
    
        
    def isEmpty(self):
        return self.head.getNext() == None
    
    
    def add(self, item):
        current = self.head.getNext()
        previous = self.head
        
        if current == None:
            temp = Node(item)
            previous.setNext(temp)
            temp.setNext(self.head)
        
        else:
            while current.getNext() != self.head:
                previous = current
                current = current.getNext()
            
            temp = Node(item)
                
            current.setNext(temp)
            temp.setNext(self.head)
        
        
    def onlyOneNode(self):
        return self.head.getNext().getNext() == self.head
    

    def remove(self, current, previous):
        if self.onlyOneNode():
            return
        
        else:
            out = current.getData()
            previous.setNext(current.getNext())
            return out
        
            
    def __str__(self):
        
        s = ""
        current = self.head.getNext()    
        count = 0
        
        while current != self.head:
            name = current.getData()
            count += 1
           
            s += name.ljust(len(name) + 2) 
            
            if count % 10 == 0:
                s += "\n"
           
            current = current.getNext()
            
        return s


def main():
    
    inFile = open("HotPotatoData.txt", "r")
    
    line = inFile.readline()
    
    #read through whole file until end is reached
    while line != "":
        line = line.strip()
        line = line.split()
        numPeople = int(line[0])
        hitCount = int(line[1])
        circle = CircularList()
        
        #make list of people in circle
        for i in range(numPeople):
            name = inFile.readline()
            name = name.strip()
            circle.add(name)
            
        #play game
        print("Hit number: {}".format(hitCount))
        print("Initial list of names ({} total):\n{}\n".format(numPeople, circle))
        
        sentinelNode = circle.head
        previous = circle.head
        current = circle.head.getNext()
        
        iteration = 1
        
        #loop until only one person remains in list
        while circle.onlyOneNode() == False:
            
            count = 1
            
            #loop until hit count is reached
            while count < hitCount:          
                previous = current
                if current.getNext() == sentinelNode:
                    previous = current.getNext()
                    current = current.getNext().getNext()
                    
                else:
                    current = current.getNext()
                
                count += 1
            
            #remove person from list and adjust list; store eliminated person's name in variable "out"
            out = circle.remove(current, previous)
            
            #set current to start counting from the person who comes after eliminated person
            if current.getNext() == sentinelNode:
                current = current.getNext().getNext()
            else:
                current = current.getNext()
            
            print("Iteration {}: {} is eliminated".format(iteration, out))
            print("Updated list:\n{}\n".format(circle))
              
            iteration += 1
        
        #once there's only one person remaining          
        print("The sole survivor is: {}\n".format(circle))
            
        line = inFile.readline()    
            
    inFile.close()

main()