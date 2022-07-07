class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print("Inside Print list method....")
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        print("Inside Append Method......")
        new_node = Node(value)
        if self.length == 0:
            print("LL is empty......")
            self.head = new_node
            self.tail = new_node
        else:
            print("Appending to LL......")
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            prev = self.head
            while temp.next is not None:
                temp = temp.next
                prev = temp
            prev.next = None
            self.tail = prev
            self.length -= 1
            return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            print("LL is empty......")
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head.next = self.head
            temp.next = None
        self.length -= 1
        return temp

if __name__ == '__main__':
    ll = LinkedList(4)
    print("creating LL>>>>>.", ll)
    check_append = ll.append(10)
    print("post append........", check_append)