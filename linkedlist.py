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
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
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
    
    def get(self, index):
        # get value at particular index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    

    def set(self, index, value):
        #cannot create index and set its value to that, works on existing index
        #sets value on existing node
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        #similarly like set it cannot create new index in start/end of LL, can insert new node in between of LL
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length-=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail #reversing head and tail
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




if __name__ == '__main__':
    ll = LinkedList(4)
    print("creating LL>>>>>.", ll)
    check_append = ll.append(10)
    print("post append........", check_append)
    check_append1 = ll.append(5)
    check_append2 = ll.append(8)
    check_append3 = ll.append(12)
    check_append4 = ll.append(17)
    ll.print_list()
    ll.reverse()
    print("reversed linked list>>>>>>")
    ll.print_list()
    ll.remove(2)
    ll.insert(2, 15)
    ll.print_list()
