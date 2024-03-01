#!/usr/bin/env python3

"""
atds.py
Creates the Stack, Queue, and Deque classes.
"""

__author__ = "Jack Naliboff"
__version__ = "1/22/24"

class Stack(object):
    
    def __init__(self):
        self.st = []
    
    def push(self, item):
        self.st.append(item)

    def pop(self):
        if len(self.st) > 0:
            return self.st.pop()

    def peek(self):
        if len(self.st) > 0:
            return self.st[-1]
        else:
            return None

    def size(self):
        return len(self.st)

    def is_empty(self):
        if len(self.st) == 0:
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.st)

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self):
        return str(self.queue)

class Deque(object):
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop(-1)

    def size(self):
        return len(self.deque)

    def is_empty(self):
        return len(self.deque) == 0
