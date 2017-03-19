# File: ERsim.py
# Description: Program simulates treatment of patients using concept of queues.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320

# Date Created: 10/12/16
# Date Last Modified: 10/12/16

#create Queue class
class Queue():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0]
        
        
#create list of lines from file; index 0 = action, index 1 = name, index 2 = queue
def createList():
    
    inFile = open("ERsim.txt", "r")

    lineList = []
    for line in inFile:
        line = line.strip()
        line = line.split()
        lineList.append(line)
    
    return lineList

    inFile.close()


#function to simulate treatment of patients
def treat():
    
    #create empty queues for each condition
    critical = Queue()
    serious = Queue()
    fair = Queue()
    
    
    #create list of lines from file given
    lst = createList()
    
    
    #iterate through list of commands
    for i in range(len(lst)) :
        
        #if action is to add patient
        if lst[i][0] == "add":
            
            name = lst[i][1]
            condition = lst[i][2]
            
            if condition == "Critical":
                critical.enqueue(name)
            if condition == "Serious":
                serious.enqueue(name)
            if condition == "Fair":
                fair.enqueue(name)
          
            
            print(">>> Add patient {} to {}".format(name, condition))
            
            print("Queues are:")
            print("  Critical: {}".format(critical.items))
            print("  Serious: {}".format(serious.items))
            print("  Fair: {}".format(fair.items))
            print()
    
    
        #if action is to treat patient
        if lst[i][0] == "treat":
            
            #if action is to treat next patient with no specification of which condition
            if lst[i][1] == "next" and len(lst[i]) == 2:
                
                allEmpty = False
                
                print(">>> Treat next patient")
                
                if not critical.isEmpty():
                    patient = critical.peek()
                    critical.dequeue()
                    print("Treating {} from Critical queue".format(patient))
                    
                else:
                    if not serious.isEmpty():
                        patient = serious.peek()
                        serious.dequeue()
                        print("Treating {} from Serious queue".format(patient))
                    else:
                        if not fair.isEmpty():
                            patient = fair.peek()
                            fair.dequeue()
                            print("Treating {} from Fair queue".format(patient))
                        else:
                            print("No patients in queues.\n")
                            allEmpty = True
                
                if not allEmpty:
                    print("Queues are:")
                    print("  Critical: {}".format(critical.items))
                    print("  Serious: {}".format(serious.items))
                    print("  Fair: {}".format(fair.items))
                    print()
                           
                
            #if action is to treat patient in specified condition
            if len(lst[i]) == 3:
                
                empty = False
                
                condition = lst[i][2]
                
                if condition == "Critical":
                    if not critical.isEmpty():
                        patient = critical.peek()
                        critical.dequeue()
                    else:
                        print("No patients in queues.\n")
                        empty = True
                    
                if condition == "Serious":
                    if not serious.isEmpty():
                        patient = serious.peek()
                        serious.dequeue()
                    else:
                        print("No patients in queues\n")
                        empty = True
                        
                if condition == "Fair":
                    if not fair.isEmpty():
                        patient = fair.peek()
                        fair.dequeue()
                    else:
                        print("No patients in queues.\n")
                        empty = True
                
                if not empty:       
                    print("Treat next patient {} from {} queue".format(patient, condition))
                    print("Treating {} from {} queue".format(patient, condition))
                    print()
             
            
            #if action is to treat all patients    
            if lst[i][1] == "all":
                print(">>> Treat all patients\n")
               
                while not critical.isEmpty():
                    patient = critical.peek()
                    critical.dequeue()
                    print("Treating {} from Critical queue".format(patient))
                    print("Queues are:")
                    print("  Critical: {}".format(critical.items))
                    print("  Serious: {}".format(serious.items))
                    print("  Fair: {}".format(fair.items))
                    print()
                
                while not serious.isEmpty():
                    patient = serious.peek()
                    serious.dequeue()
                    print("Treating {} from Critical queue".format(patient))
                    print("Queues are:")
                    print("  Critical: {}".format(critical.items))
                    print("  Serious: {}".format(serious.items))
                    print("  Fair: {}".format(fair.items))
                    print()
 

                while not fair.isEmpty():
                    patient = fair.peek()
                    fair.dequeue()
                    print("Treating {} from Critical queue".format(patient))
                    print("Queues are:")
                    print("  Critical: {}".format(critical.items))
                    print("  Serious: {}".format(serious.items))
                    print("  Fair: {}".format(fair.items))
                    print()                          
    
    
        #if action is to exit...
        if lst[i][0] == "exit":
            print(">>> Exit")
            return
    
    
def main():

    treat()

main()