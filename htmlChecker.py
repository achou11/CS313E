# File: htmlChecker.py
# Description: Program checks to see if an html file is valid.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320

# Date Created: 10/3/16
# Date Last Modified: 10/7/16


#create Stack class
class Stack():
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


#function to identify and create list of tags in file
def getTag(string, tagList):
      
    closed = False
    
    for i in range(0, len(string)-1):
        if string[i] == "<":
            tag = ""
            start = i+1
            for j in range(start, len(string)-1):
                if string[j] == ">" or string[j] == " ":
                    closed = True
                    break

                else:             
                    if ">" not in string[j:]:
                        break
                    else:
                        tag += string[j]
                    
            if closed:
                
                tagList.append(tag)

    #remove any tag that is incomplete i.e. <a...
    for i in range(tagList.count("")):
        tagList.remove("")
    
    #remove any tag that contains < in it i.e. <a< ...    
    for el in tagList:
        if "<" in el:
            tagList.remove(el)
        
    return tagList
 

#function to check if tag list is valid for html file
def tagChecker(tList):
    
    s = Stack()
    balanced = True
    index = 0
 
    #create empty list of valid tags that will be filled
    VALIDTAGS = []
    
    #create empty list of exception tags that will be filled
    EXCEPTIONS = []
    exCheck_tList = []
    
    #look through tag list to check if there are any exceptions; update exceptions list as you iterate
    for t in tList:
        if "/" not in t:
            exCheck_tList.append(t)
        else:
            t_prime = t[1:]
            exCheck_tList.append(t_prime)
    
    for t in exCheck_tList:
        if (exCheck_tList.count(t) % 2 != 0) and (t not in EXCEPTIONS):
                EXCEPTIONS.append(t)
                
    EXCEPTIONS.sort()
    
    #begin tag-checking process
    while index < len(tList) and balanced:
 
        tag = tList[index]

        #add to VALIDTAG list as you iterate through tag list
        if tag not in VALIDTAGS and tag not in EXCEPTIONS:
            VALIDTAGS.append(tag)
            print("New tag {} found and added to list of valid tags.".format(tag))
            
        #if tag is a start tag...
        if "/" not in tag:
            if tag in EXCEPTIONS:
                print("Tag {} does not need match: stack is still {}".format(tag, s.items))
            else:
                s.push(tag)
                print("Tag {} pushed: stack is now {}".format(tag, s.items))
        
        #if tag is an end tag...  
        else:   
            if s.isEmpty():
                print("Error: tag is {} but there is nothing on the stack. Terminating.".format(tag))
                return
            else:
                top = s.pop()
                #if top item in stack doesn't match end tag being checked...
                if top != tag[1:]: 
                    balanced = False
                    print("Error: tag is {} but top of stack is {}".format(tag, top))
                    return
                else:
                    print("Tag {} matches top of stack: stack is now {}".format(tag, s.items))
        index += 1
 

    #if html file is valid...
    if balanced and s.isEmpty():
        print("\nProcessing complete. No mismatches found.\n")
    
    #if html file is invalid...   
    else:
        print("\nProcessing complete. Unmatched tags remain on stack: {}\n".format(s.items))


    VALIDTAGS.sort()
        
    print("Valid tags found in file: {}\n".format(VALIDTAGS))
    print("Exceptions in file: {}".format(EXCEPTIONS))


#function to create list of tags found in file
def createTagList():
    
    inFile = open("htmlFile.txt", "r")

    tagList = []
    for line in inFile:
        getTag(line,tagList)
    
    return tagList

    inFile.close()


def main():

    #create list of tags from file
    tag_list = createTagList()

    print(tag_list, "\n")

    #check to to see if file is valid html file
    tagChecker(tag_list)
    
main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        