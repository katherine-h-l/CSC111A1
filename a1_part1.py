"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

This Python module contains three linked list subclasses corresponding to the three
moving heuristics described on the assignment handout.

You need to complete their implementations by overriding the __contains__ method
(and only for CountLinkedList, additional methods as required).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Isaac Waller.
The assignment was written by Zaina Azhar and Katherine Luo. 
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional

from a1_linked_list import LinkedList, _Node


################################################################################
# Heuristic 1 (move to front)
################################################################################
class MoveToFrontLinkedList(LinkedList):
    """A linked list implementation that uses a "move to front" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """
    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, move it to the front of this list.

        >>> linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        >>> linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(10)
        True
        >>> linky.to_list()
        [10, 20, 30, 40, 50, 60]
        """
        if self._first is None:
            return False

        elif self._first.item == item:
            return True

        else:
            prev, curr = None, self._first
            while curr is not None:
                if curr.item == item:
                    prev.next = curr.next
                    self._first, curr.next = curr, self._first
                    return True

                prev, curr = curr, curr.next

            return False


################################################################################
# Heuristic 2 (swap)
################################################################################
class SwapLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique
    """
    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, swap it with the item before it, if any.
        You may do this by reassigning _Node item or next attributes (or both).

        >>> linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [10, 20, 40, 30, 50, 60]
        >>> linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(10)
        True
        >>> linky.to_list()
        [10, 20, 30, 40, 50, 60]
        """
        if self._first is None:
            return False

        elif self._first.item == item:
            return True

        else:
            prev, curr = None, self._first
            while curr is not None:
                if curr.item == item:
                    prev.item, curr.item = curr.item, prev.item
                    return True

                prev, curr = curr, curr.next

            return False


################################################################################
# Heuristic 3 (count)
################################################################################
# NOTE: this heuristic requires a new kind of _Node that has an additional "count" attribute.
@dataclass
class _CountNode(_Node):
    """A node in a CountLinkedList.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
      - access_count: The number of times this node has been accessed (used by the count heuristic)
    """
    next: Optional[_CountNode] = None
    access_count: int = 0


class CountLinkedList(LinkedList):
    """A linked list implementation that uses a "swap" heuristic for searches.

    Representation Invariants:
        - all items in this linked list are unique

    NOTE: In order to make use of the _CountNode class above, you'll need to override every
    LinkedList method in a1_linked_list.py that creates new _Node objects to create _CountNode
    objects instead. Your code for the overridden methods should be otherwise identical.
    """
    _first: Optional[_CountNode]

    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list.
        """
        new_node = _CountNode(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        If the item is found, increase its count and reorder the nodes in
        non-increasing count order---see assignment handout for details.

        >>> linky = CountLinkedList([10, 20, 30, 40, 50, 60])
        >>> linky.__contains__(40)
        True
        >>> linky.to_list()
        [40, 10, 20, 30, 50, 60]
        """
        contains_item = False
        if self._first is None:
            return False

        elif self._first.item == item:
            self._first.access_count += 1
            return True

        else:
            prev_shift, node_shift = None, None
            prev, curr = None, self._first
            while curr is not None:
                if curr.item == item:
                    prev_shift, node_shift = prev, curr
                    node_shift.access_count += 1
                    contains_item = True
                prev, curr = curr, curr.next

            if node_shift is None:
                return contains_item

            elif self._first.access_count < node_shift.access_count:
                prev_shift.next, self._first, node_shift.next = \
                    node_shift.next, node_shift, self._first
                return contains_item

            elif prev_shift.access_count >= node_shift.access_count > node_shift.next.access_count:
                return contains_item

            else:
                prev_2, curr_2 = self._first, self._first.next
                while curr_2 is not None:
                    if prev_2.access_count >= node_shift.access_count > curr_2.access_count:
                        prev_shift.next, prev_2.next, node_shift.next = \
                            node_shift.next, node_shift, prev_2.next

                    prev_2, curr_2 = curr_2, curr_2.next

            return contains_item


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136'],
        'extra-imports': ['a1_linked_list'],
        'max-nested-blocks': 4
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
