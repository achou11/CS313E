# File: ExpressionTrees.py
# Description: Program evaluates mathematical expressions to return value and prefix and postfix notation.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E
# Unique Number: 51320

# Date Created: 12/1/16
# Date Last Modified: 12/1/16

#create Stack class for evaluating tree
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)


#create BinaryTree class to create tree from expression
class BinaryTree(object):
    
    def __init__(self, initVal = None):
        self.data = initVal
        self.left = None
        self.right = None


    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t


    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t


    def getLeftChild(self):
        return self.left


    def getRightChild(self):
        return self.right


    def setRootVal(self,value):
        self.data = value


    def getRootVal(self):
        return self.data


    def __str__(self):
        return self.data


    #create tree for expression
    def createTree (self, expr):
        
        #create list of elements in expression
        expr = expr.split()
        
        operators = "+-*/"

        st = Stack()

        for token in expr:
            
            if token == "(":
                self.left = BinaryTree()
                st.push(self)
                self = self.left
                
            elif token == ")":
                if not(st.isEmpty()):
                    self = st.pop()
                    
            elif token in operators:
                self.setRootVal(token)
                st.push(self)
                self.right = BinaryTree()
                self = self.right
                
            else:
                self.setRootVal(token)
                self = st.pop()


    #get value for expression
    def evaluate(self):
         
        operators = "+-*/"
        
        if self.getRootVal() == None:
            return 0
        
        elif self.getRootVal() not in operators:
            return float(self.getRootVal())
        
        else:
            if self.getRootVal() == "+":
                return self.getLeftChild().evaluate() + self.getRightChild().evaluate()
            
            elif self.getRootVal() == "-":
                return self.getLeftChild().evaluate() - self.getRightChild().evaluate()
            
            elif self.getRootVal() == "*":
                return self.getLeftChild().evaluate() * self.getRightChild().evaluate()
            
            elif self.getRootVal() == "/":
                return self.getLeftChild().evaluate() / self.getRightChild().evaluate() 
    

    #get prefix notation for expression
    def preOrder(self):
        
        print(self.data, end = " ")
        
        if self.left != None:

            self.getLeftChild().preOrder()
            
        if self.right != None:
            self.getRightChild().preOrder()
    
      
    #get postfix notation for expression
    def postOrder(self):
        
        if self.left != None :
            self.getLeftChild().postOrder()
        
        if self.right != None:
            self.getRightChild().postOrder()
        
        print(self.data, end = " ")

    
def main():

    #open file with expressions
    file = open("treedata.txt", "r")

    #read through each line in file and evaluate
    for line in file:
        
        line.strip()

        tree = BinaryTree()
        tree.createTree(line)
        result = tree.evaluate()
        
        print("Infix expression: {}".format(line))
        
        print("  Value: {}".format(result))
        
        print("  Prefix expression: ", end = " ")
        tree.preOrder()
        
        print("\n  Postfix expression: ", end = " ")
        tree.postOrder()

        print("\n")
    
    #close file
    file.close()

main()

