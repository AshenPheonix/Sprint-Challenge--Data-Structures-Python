from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right=BinarySearchTree(value)
        else:
            self.count+=1

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value==target:
            return True
        elif self.value < target and self.right:
            return self.right.contains(target)
        elif self.value > target and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        temp_node = node
        while temp_node:
            print(temp_node.value)
            if temp_node.left:
                queue.enqueue(temp_node.left)
            if temp_node.right:
                queue.enqueue(temp_node.right)
            temp_node=queue.dequeue()

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        temp_node = node
        while temp_node:
            print(temp_node.value)
            if temp_node.left:
                stack.push(temp_node.left)
            if temp_node.right:
                stack.push(temp_node.right)
            temp_node = stack.pop()

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self)
        if self.right:
            self.right.pre_order_dft(self)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self)
        if self.right:
            self.right.post_order_dft(self)
        print(self.value)

    def delete_target(self, back, removed):
        if self.right:
            self.right.delete_target(self,removed)
        else:
            removed.value = self.value
            back.right = self.left
        
    def delete(self, value_to_remove):
        if self.value == value_to_remove:
            self.left.delete_target(self,self)
        elif self.value < value_to_remove:
            self.right.delete(value_to_remove)
        else:
            self.left.delete(value_to_remove)

    def get_copies(self, arr):
        if self.count>1:
            arr.append(self.value)
        if self.left:
            self.left.get_copies(arr)
        if self.right:
            self.right.get_copies(arr)