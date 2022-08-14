#Binary Search Tree using Python


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
    
    # def print_nodes(self):
    #     temp = self.root
    #     while temp is not None:
    #         print("temp>>>",temp)
    #         temp = temp.next

    def insert_node(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        temp = self.root
        if new_node.value == temp.value:
            return False
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left = new_node
                return True
            else:
                temp = temp.left
        else:
            if temp.right is None:
                temp.right = new_node
                return True
            temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if temp.value < value:
                temp = temp.left
            elif temp.value > value:
                temp = temp.right
            else:
                return True
            return False
    
    def minimum_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

new_node = BST(4)
x = new_node.insert_node(5)
x = new_node.insert_node(10)
x = new_node.insert_node(2)
#work on method to print all nodes in BST

