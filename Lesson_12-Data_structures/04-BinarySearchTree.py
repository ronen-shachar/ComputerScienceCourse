from typing import Any

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: Any):
        """
        Inserts a new node with the given value into the binary search tree.
        
        This is a wrapper method that calls the recursive _insert method with the root node of the tree.
        
        Args:
            value (Any): The value to insert into the binary search tree.
        """
        self.root = self._insert(value, self.root)

    def _insert(self, value: Any, node: Node):
        """
        Recursively inserts a new node with the given value into the binary search tree.
        
        If the current node is None, creates a new node with the given value.
        If the value is less than the current node's value, recursively inserts the value into the left subtree.
        If the value is greater than or equal to the current node's value, recursively inserts the value into the right subtree.
        Returns the updated node after the insertion.
        
        Args:
            value (Any): The value to insert into the binary search tree.
            node (Node): The current node in the binary search tree.
        
        Returns:
            BinaryTreeNode: The updated node after the insertion.
        """
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)
        return node

    def find(self, value: Any) -> bool:
        """
        Searches for the given value in the binary search tree.

        This is a wrapper method that calls the recursive _find method with the root node of the tree.
        
        Args:
            value (Any): The value to search for in the tree.
        
        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        return self._find(value, self.root)

    def _find(self, value, node: Node) -> bool:
        """
        Recursively searches for the given value in the binary search tree rooted at the provided node.
        
        if the current node is None, returns False (Base case).
        If the value is equal to the current node's value, returns True (Base case).
        If the value is less than the current node's value, recursively searches the left subtree.
         else recursively searches the right subtree.

        Args:
            value (Any): The value to search for in the tree.
            node (Node): The root node of the subtree to search.
        
        Returns:
            bool: True if the value is found in the tree, False otherwise.
        """
        if node is None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            return self._find(value, node.left)
        else:
            return self._find(value, node.right)
            
    def delete(self, value: Any) -> bool:
        """
        Deletes the node with the given value from the binary search tree.
        Update the root of the tree to point to the new root after the deletion.
    
        This is a wrapper method that calls the recursive _delete method with the root node of the tree.
        
        Args:
            value (Any): The value to delete from the tree.
        
        Returns:
            bool: True if the value is found in the tree, False otherwise.
         """
        self.root, deleted = self._delete(value, self.root)
        return deleted

    def _delete(self, value: Any, node: Node):
        """
        Recursively deletes a node with the given value from the binary search tree.

        if the current node is None, returns False (Base case).
        if the value is less than the current node's value, recursively deletes the value from the left subtree.
        if the value is greater than the current node's value, recursively deletes the value from the right subtree.
        if the value is equal to the current node's value, deletes the current node and returns the updated node.
            if the current node has no children, set the current node to None.
            if the current node has only one child, set the current node to the child.
            if the current node has two children,
                find the successor value of the current node
                and replace the current node's value with the successor's value.
                then recursively delete the node with the successor value.
        return the updated node.

        Args:
            value (Any): The value to be deleted.
            node (Node): The current node being processed.
        
        Returns:
            Tuple[Node, bool]: The updated node after deletion, and a boolean indicating whether the value was deleted.
        """
        if node is None:
            return None, False
        elif value < node.value:
            node.left, deleted = self._delete(value, node.left)
        elif value > node.value:
            node.right, deleted = self._delete(value, node.right)
        else:
            # Value is equal to the current node's value
            # we have found the node to be deleted
            # deleted is set to True
            deleted = True

            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                # node has two children. Find the successor of the current node.
                successor = self._find_min(node.right)
                node.value = successor.value
                # recursively delete the successor node.
                # We can ignore the deleted return value because we are deleting the node with the value equal to the successor's value.
                node.right, deleted_to_be_ignored = self._delete(successor.value, node.right)
        return node, deleted
    
    def _find_min(self, node: Node) -> Node:
        """
        Finds the node with the minimum value in the given binary search tree node.
        
        Args:
            node (Node): The root node of the binary search tree to search.
        
        Returns:
            Node: The node with the minimum value in the given binary search tree.
        """
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)
        
    def print(self):
        def _print_with_indent(node, indent, edge):
            if node is not None:
                _print_with_indent(node.right, indent + 4, '/-')
                print(" " * indent, edge, node.value, sep='')
                _print_with_indent(node.left, indent + 4, '\\-')

        if self.root is not None:
            _print_with_indent(self.root, 0, '-')
        else:
            print('Empty tree')



# Tests
tree = BinarySearchTree()
tree.insert(5)
tree.print()
print('Test delete 5', tree.delete(5))
print('Test delete non-existing 3', tree.delete(3))
tree.print()

tree = BinarySearchTree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.print()
print('Test delete 5', tree.delete(5))
tree.print()
print()

tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(2)

tree.print()
print('Find 4', tree.find(4))  # True
print('Find 6', tree.find(6))  # False

# Delete
print()
print('Delete 5 test')
print('Before delete')
tree.print()
print('Test delete 5', tree.delete(5))
print('After delete')
tree.print()
print(tree.find(5))  # False
print(tree.find(3))  # True

print()
print('Delete 4 test')
print('Before delete')
tree.print()
print('Test delete 4', tree.delete(4))
print('After delete')
tree.print()
print(tree.find(4))  # False
print(tree.find(7))  # True
print(tree.find(3))  # True

print()
print('Delete 1 test')
print('Before delete')
tree.print()
print('Test delete 1', tree.delete(1))
print('After delete')
tree.print()
print(tree.find(1))  # False