#Queue in Python (FIFO)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    

    def print_queue(self):
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        self.length +=1
        return new_node
    

    def dequeue(self):
        # doubt not working as FIFO
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -=1
        return temp



new_queue = Queue(5)
new_queue.print_queue()
print("Started enqueue.....")
new_queue.enqueue(4)
new_queue.enqueue(3)
new_queue.enqueue(8)
print("After enqueue.....")
new_queue.print_queue()
new_queue.dequeue()
print("After dequeue.....")
new_queue.print_queue()