"""CSC111 Winter 2021 Assignment 1: Linked Lists, Part 1

Instructions (READ THIS FIRST!)
===============================

Please write your tests for Part 1 in this module. Make sure to review the assignment
instructions carefully for this part! You may find it helpful to consult this
section of the Course Notes:
https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html

While you must include unit tests, you may also use property-based tests in your test suite.

We will *not* be running PythonTA on this file; however, you should follow good programming
design and style in this file anyway, just like you would for all other work.

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
import pytest
from a1_part1 import MoveToFrontLinkedList, SwapLinkedList, CountLinkedList

# Test 1) MoveToFrontLinkedList #


def test_move_return_1() -> None:
    """Test that the __contains__ method return the correct value
    with one node
    """
    linky = MoveToFrontLinkedList([10])
    assert linky.__contains__(10) is True


def test_move_mutate_1() -> None:
    """Test that the __contains__ method doesnt mutate
    with one node
    """
    linky = MoveToFrontLinkedList([10])
    linky.__contains__(10)
    linky_list = linky.to_list()
    assert linky_list == [10]


def test_move_return_2() -> None:
    """Test that the __contains__ method return the correct value
    with 2 nodes
    """
    linky = MoveToFrontLinkedList([10, 20])
    assert linky.__contains__(20) is True


def test_move_mutate_2() -> None:
    """Test that the __contains__ method mutates
    with 2 nodes
    """
    linky = MoveToFrontLinkedList([10, 20])
    linky.__contains__(20)
    linky_list = linky.to_list()
    assert linky_list == [20, 10]


def test_move_return_true_3() -> None:
    """Test that the __contains__ method returns True
    """
    linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
    assert linky.__contains__(30) is True


def test_move_mutate_3() -> None:
    """Test that the __contains__ method mutates
    """
    linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(30)
    linky_list = linky.to_list()
    assert linky_list == [30, 10, 20, 40, 50, 60]


def test_move_return_false_4() -> None:
    """Test that the __contains__ method returns False
    """
    linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
    assert linky.__contains__(100) is False


def test_move_mutate_4() -> None:
    """Test that the __contains__ method doesnt mutate when
    False
    """
    linky = MoveToFrontLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == [10, 20, 30, 40, 50, 60]


def test_move_return_5() -> None:
    """Test that the __contains__ method returns False
    with an empty list
    """
    linky = MoveToFrontLinkedList([])
    assert linky.__contains__(100) is False


def test_move_mutate_5() -> None:
    """Test that the __contains__ method doesn't mutate with
    an empty list
    """
    linky = MoveToFrontLinkedList([])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == []


# Test 2) SwapLinkedList #


def test_swap_return_1() -> None:
    """Test that the __contains__ method returns the correct value
    with one node
    """
    linky = SwapLinkedList([10])
    assert linky.__contains__(10) is True


def test_swap_mutate_1() -> None:
    """Test that the __contains__ method doesn't mutate with
    one node
    """
    linky = SwapLinkedList([10])
    linky.__contains__(10)
    linky_list = linky.to_list()
    assert linky_list == [10]


def test_swap_return_2() -> None:
    """Test that the __contains__ method returns the correct value
    with 2 nodes
    """
    linky = SwapLinkedList([10, 20])
    assert linky.__contains__(20) is True


def test_swap_mutate_2() -> None:
    """Test that the __contains__ method mutates with 2 nodes
    """
    linky = SwapLinkedList([10, 20])
    linky.__contains__(20)
    linky_list = linky.to_list()
    assert linky_list == [20, 10]


def test_swap_return_true_3() -> None:
    """Test that the __contains__ method returns True
    """
    linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
    assert linky.__contains__(30) is True


def test_swap_mutate_3() -> None:
    """Test that the __contains__ method mutates correctly
    """
    linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(30)
    linky_list = linky.to_list()
    assert linky_list == [10, 30, 20, 40, 50, 60]


def test_swap_return_false_4() -> None:
    """Test that the __contains__ method returns False
    """
    linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
    assert linky.__contains__(100) is False


def test_swap_mutate_4() -> None:
    """Test that the __contains__ method doesn't mutate
    when False
    """
    linky = SwapLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == [10, 20, 30, 40, 50, 60]


def test_swap_return_5() -> None:
    """Test that the __contains__ method returns False with
    an empty list
    """
    linky = SwapLinkedList([])
    assert linky.__contains__(100) is False


def test_swap_mutate_5() -> None:
    """Test that the __contains__ method doesn't mutate with
    an empty list
    """
    linky = SwapLinkedList([])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == []

# Test 3) CountLinkedList #


def test_count_multi_calls_1() -> None:
    """Test that the __contains__ method mutates the order correctly
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(50)
    linky_list = linky.to_list()
    assert linky_list == [40, 50, 10, 20, 30, 60]


def test_count_mutate_1_a() -> None:
    """Test that the __contains__ method mutates the access count of 40
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(50)
    assert linky._first.access_count == 3


def test_count_mutate_1_b() -> None:
    """Test that the __contains__ method mutates the access count of 50
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(50)
    assert linky._first.next.access_count == 1


def test_count_multi_calls_2() -> None:
    """Test that the __contains__ method mutates the order correctly when
    the last node is called
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(40)
    linky.__contains__(40)
    linky.__contains__(60)
    linky_list = linky.to_list()
    assert linky_list == [40, 60, 10, 20, 30, 50]


def test_count_mutate_2() -> None:
    """Test that the __contains__ method mutates the order correctly when
    the first node is called
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(10)
    linky_list = linky.to_list()
    assert linky_list == [10, 20, 30, 40, 50, 60]


def test_count_return_false_3() -> None:
    """Test that the __contains__ method returns False
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    assert linky.__contains__(100) is False


def test_count_mutate_3() -> None:
    """Test that the __contains__ method doesn't mutate
    when False
    """
    linky = CountLinkedList([10, 20, 30, 40, 50, 60])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == [10, 20, 30, 40, 50, 60]


def test_count_empty_return_4() -> None:
    """Test that the __contains__ method returns False with
    an empty list
    """
    linky = CountLinkedList([])
    assert linky.__contains__(100) is False


def test_count_empty_mutate_4() -> None:
    """Test that the __contains__ method doesn't mutate with
    an empty list
    """
    linky = CountLinkedList([])
    linky.__contains__(100)
    linky_list = linky.to_list()
    assert linky_list == []


def test_count_one_return_5() -> None:
    """Test that the __contains__ method returns the correct value
    with one node
    """
    linky = CountLinkedList([10])
    assert linky.__contains__(10) is True


def test_count_one_mutate_5() -> None:
    """Test that the __contains__ method doesn't mutate with one node
    """
    linky = CountLinkedList([10])
    linky.__contains__(10)
    linky_list = linky.to_list()
    assert linky_list == [10]


def test_count_two_return_6() -> None:
    """Test that the __contains__ method returns the correct value
    with 2 nodes
    """
    linky = CountLinkedList([10, 20])
    assert linky.__contains__(20) is True


def test_count_two_mutate_6() -> None:
    """Test that the __contains__ method mutates with 2 nodes
    """
    linky = CountLinkedList([10, 20])
    linky.__contains__(20)
    linky_list = linky.to_list()
    assert linky_list == [20, 10]


if __name__ == '__main__':
    pytest.main(['a1_part1_test.py', '-v'])
