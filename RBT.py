#!/bin/python3

class red_black_tree:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, val):
        if val is None:
            print("Can't insert None value")
            return None

        if self.val is None:
            self.val = val

        elif val == self.val:
            print("Duplicate val")
        elif val < self.val:
            self.left = self.left.insert(
                val) if self.left else red_black_tree(val)
            self.left.parent = self
        else:
            self.right = self.right.insert(
                val) if self.right else red_black_tree(val)
            self.right.parent = self
        return self

    def preorder(self):
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
