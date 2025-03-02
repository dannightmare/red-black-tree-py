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
                val) if self.left else red_black_tree(val, parent=self)
        else:
            self.right = self.right.insert(
                val) if self.right else red_black_tree(val, parent=self)
        return self

    def preorder(self):
        print(self.val)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def left_rotate(self):
        x = self.right
        if x is None:
            print("Can't rotate left")
            return self

        x.parent = self.parent
        self.right = x.left
        if self.right:
            self.right.parent = self

        x.left = self
        self.parent = x

        return x


def test_left_rotate_1():
    t = red_black_tree()
    t.insert(1)
    t.insert(0)
    t.insert(2)

    t = t.left_rotate()

    assert (t.val == 2)
    assert (t.left.val == 1)
    assert (t.left.left.val == 0)

    assert (t.left.parent == t)
    assert (t.left.left.parent == t.left)
