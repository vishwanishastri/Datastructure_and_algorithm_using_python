#Tree Traversal using Python
#converts BST Into Linked List
# More complicated then Linked list as in a tree there are multiple ways to access each node which is called Breadth first search
#BFS start from starting first node
# or start from bottom left then go up and search on right side till its bottom which is called Depth first search 


#BFS(Breadth first search)

# create 2 list queue and results
# in queue start from top and store that node in queue
#store values of node in results
#if queue is empty then it mean we visited all items in a tree as all values are eventually node of a tree
#continued class of binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert_node(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
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

    def BFS(self):
        current_node = self.root
        queue=[]
        results=[]
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    
    def dfs_pre_order(self):
        # DFS(Dept First Search)
        #Type 1: Preorder -- add number to list from top to left and then to right
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results
    
    def dfs_postorder(self):
        #Type 2:Post Order--> Starts with top bt we are not going to right results to results list while traversing
        # differe is we are going to append later after traversing to left/rigths
        results =[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results
    
    def dfs_inorder(self):
        #Type3: Inorder -->   Vist first node, then move to extreme left and append value then go to right
        # whereas in postorder it used to go both on left and right then append value     
        # output will be in numerical order
        results =[]
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

op = BST()
op.insert_node(10)
op.insert_node(5)
op.insert_node(25)
op.insert_node(65)
op.insert_node(82)
op.insert_node(27)
op.insert_node(18)

print(op.BFS())

print(op.dfs_pre_order())
print(op.dfs_postorder())
print(op.dfs_inorder())

