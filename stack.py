# Stack in Python (LIFO)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.bottom = new_node
        self.height = 1
    
    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
    

    def push(self,value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return new_node
    

    def pop(self):
        if self.height is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height +=1
        return temp


new_stack = Stack(5)
new_stack.print_stack()
print("Started push.....")
new_stack.push(4)
new_stack.push(3)
new_stack.push(8)
print("After push.....")
new_stack.print_stack()
new_stack.pop()
print("After pop.....")
new_stack.print_stack()




    