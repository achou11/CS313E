#implementation of Stack class using list


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



def main():
    
    
    s = Stack()
    
    s.push("Yes")
    
    s.push(2)
    
    print(s.size())
    
    print(s.items)


main()