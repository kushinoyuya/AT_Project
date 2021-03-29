from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, next_node: Node = None)
        self.data = data
        self.next = next_node

class LinkedList(object):
    def __init__(self, head=None) -> None:
        self.head = head
