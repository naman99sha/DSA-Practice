import BinaryTreeNode
class BinarySearchTree():
    root = None
    def __init__(self) -> None:
        self.root = None
    def insert(self,val):
        if self.root == None:
            self.root = BinaryTreeNode.BinaryTreeNode(val)
            return
        else:
            temp = self.root
            while not temp == None:
                if val <= temp.val:
                    if not temp.left == None:
                        temp = temp.left
                    else:
                        temp.left = BinaryTreeNode.BinaryTreeNode(val)
                        return
                else:
                    if not temp.right == None:
                        temp = temp.right
                    else:
                        temp.right = BinaryTreeNode.BinaryTreeNode(val)
                        return

    def lookup(self,val):
        if self.root == None:
            return None
        temp = self.root
        while not temp.val == val and not temp == None:
            if val <= temp.val:
                temp = temp.left
            else:
                temp = temp.right
            if temp == None:
                break
            if temp.val == val:
                return True
        return False
    
    def remove(self, data):
        if not self.root:
            print("Empty Tree!")

        else:

            curr_node = self.root
            prev_node = curr_node

            while(data):

                if curr_node.val == data:

                    # No right child and left child
                    if not curr_node.left and not curr_node.right:
                        
                        if curr_node is prev_node.left:
                            prev_node.left = None
                            del curr_node
                            data = None
                        else:
                            prev_node.right = None
                            del curr_node
                            data = None

                    # No right child
                    elif not curr_node.right:
                        if curr_node is prev_node.left:
                            prev_node.left = curr_node.left
                            del curr_node
                            data = None
                        else:
                            prev_node.right = curr_node.left
                            del curr_node
                            data = None

                    # Right child
                    elif curr_node.right:
                        temp1 = prev_node
                        temp2 = curr_node.left
                        temp3 = curr_node.right
                        temp4 = curr_node
                        
                        prev_node = curr_node
                        curr_node = curr_node.right

                        while(curr_node.left):
                            prev_node = curr_node
                            curr_node = curr_node.left

                        if temp1.left is temp4:
                            temp1.left = curr_node
                        elif temp1.right is temp4:
                            temp1.right = curr_node
                        else:
                            self.root = curr_node

                        curr_node.left = temp2
                        curr_node.right = temp3
                        
                        if curr_node.right is curr_node:
                            curr_node.right = None
                        else:
                            prev_node.left = None

                        del temp4
                        data = None
                
                elif curr_node.val < data:
                    if curr_node.right:
                        prev_node = curr_node
                        curr_node = curr_node.right
                    else:
                        print('Value not in Tree')
                        data = None

                elif curr_node.val > data:
                    if curr_node.left:
                        prev_node = curr_node
                        curr_node = curr_node.left
                    else:
                        print('Value not in Tree')
                        data = None
                
                
def traverse(node):
    tree = {"val" : node.val}
    tree["left"] = None if node.left == None else traverse(node.left)
    tree["right"] = None if node.right == None else traverse(node.right)
    return tree

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(1)
tree.insert(20)
tree.insert(15)
tree.insert(170)
tree.remove(9)
print(traverse(tree.root))
print(tree.lookup(5))
"""
            9
    4               20
1        6      15      170

"""
