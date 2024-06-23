from ..linked_list import LinkedList
import pytest


def test_create_linked_list_with_value():
    ll = LinkedList(23)
    assert ll.length == 1
    assert ll.head == ll.tail
    assert ll.head is not None
    assert ll.head.next is None
    assert ll.head.value == 23


def test_create_empty_linked_list():
    ll = LinkedList(None)
    assert ll.length == 0
    assert ll.head == ll.tail
    assert ll.head is None


def test_append_on_empty_linked_list():
    ll = LinkedList(None)
    result = ll.append(23)
    assert result
    assert ll.length == 1
    assert ll.head == ll.tail
    assert ll.head is not None
    assert ll.head.next is None
    assert ll.head.value == 23


def test_append_on_not_empty_linked_list():
    ll = LinkedList(1)
    result = ll.append(23)
    assert result
    assert ll.length == 2
    assert ll.head.value == 1
    assert ll.tail.value == 23
    assert ll.head.next.value == 23
    assert ll.tail.next is None


def test_pop_on_empty_linked_list():
    ll = LinkedList(None)
    node = ll.pop()
    assert node is None
    assert ll.head == ll.tail
    assert ll.head is None
    assert ll.length == 0


def test_pop_on_linked_list_with_one_element():
    ll = LinkedList(23)
    node = ll.pop()
    assert ll.length == 0
    assert ll.head == ll.tail
    assert ll.head is None
    assert node.value == 23
    assert node.next is None


def test_pop_on_linked_list_with_three_elements():
    ll = LinkedList(20)
    ll.append(25)
    ll.append(30)
    node = ll.pop()
    assert ll.length == 2
    assert ll.head.value == 20
    assert ll.tail.value == 25
    assert ll.tail.next is None
    assert node.value == 30
    assert node.next is None


def test_preppend_on_empty_list():
    ll = LinkedList(None)
    result = ll.preppend(1)
    assert result
    assert ll.length == 1
    assert ll.head == ll.tail
    assert ll.head.value == 1
    assert ll.tail.next is None


def test_preppend_on_list_with_one_element():
    ll = LinkedList(1)
    result = ll.preppend(2)
    assert result
    assert ll.length == 2
    assert ll.head.value == 2
    assert ll.tail.value == 1
    assert ll.tail.next is None


def test_pop_first_on_empty_list():
    ll = LinkedList(None)
    node = ll.pop_first()
    assert node is None
    assert ll.head == ll.tail
    assert ll.head is None
    assert ll.length == 0


def test_pop_first_on_linked_list_with_one_element():
    ll = LinkedList(23)
    node = ll.pop_first()
    assert ll.length == 0
    assert ll.head == ll.tail
    assert ll.head is None
    assert node.value == 23
    assert node.next is None


def test_pop_first_on_linked_list_with_three_elements():
    ll = LinkedList(20)
    ll.append(25)
    ll.append(30)
    node = ll.pop_first()
    assert ll.length == 2
    assert ll.head.value == 25
    assert ll.tail.value == 30
    assert ll.tail.next is None
    assert node.value == 20
    assert node.next is None


@pytest.mark.parametrize("index", [1, 0, -1])
def test_get_invalid_index(index):
    ll = LinkedList(None)
    result = ll.get(index)
    assert result is None


def test_get_valid_index():
    ll = LinkedList(1)
    node = ll.get(0)
    assert node is not None
    assert node.value == 1
    assert ll.length == 1
    assert ll.head == ll.tail
    assert ll.tail.next is None


@pytest.mark.parametrize("index", [0, 1, -1])
def test_set_value_invalid_index(index):
    ll = LinkedList(None)
    result = ll.set_value(index, 1)
    assert result is False


def test_set_value_valid_index():
    ll = LinkedList(1)
    result = ll.set_value(0, 1)
    assert result is True
    assert ll.length == 1
    assert ll.head == ll.tail
    assert ll.head.value == 1
    assert ll.tail.next is None


@pytest.mark.parametrize("index", [1, -1])
def test_insert_invalid_index(index):
    ll = LinkedList(None)
    result = ll.insert(index, 1)
    assert result is False
    assert ll.length == 0
    assert ll.head is None
    assert ll.tail is None


def test_insert_on_list_head():
    ll = LinkedList(2)
    result = ll.insert(0, 1)
    assert result is True
    assert ll.length == 2
    assert ll.head.value == 1
    assert ll.tail.value == 2
    assert ll.tail.next is None


def test_insert_on_list_tail():
    ll = LinkedList(1)
    result = ll.insert(1, 2)
    assert result is True
    assert ll.length == 2
    assert ll.head.value == 1
    assert ll.tail.value == 2
    assert ll.tail.next is None


def test_insert_on_list_middle():
    ll = LinkedList(1)
    ll.append(3)
    result = ll.insert(1, 2)
    assert result is True
    assert ll.length == 3
    assert ll.head.value == 1
    assert ll.tail.value == 3
    assert ll.tail.next is None
    assert ll.get(1).value == 2


@pytest.mark.parametrize("index", [1, -1])
def test_remove_invalid_index(index):
    ll = LinkedList(1)
    result = ll.remove(index)
    assert result is None
    assert ll.length == 1
    assert ll.head.value == 1
    assert ll.tail.value == 1
    assert ll.tail.next is None


def test_remove_on_list_head():
    ll = LinkedList(23)
    node = ll.remove(0)
    assert ll.length == 0
    assert ll.head == ll.tail
    assert ll.head is None
    assert node.value == 23
    assert node.next is None


def test_remove_on_list_tail():
    ll = LinkedList(23)
    node = ll.remove(0)
    assert ll.length == 0
    assert ll.head == ll.tail
    assert ll.head is None
    assert node.value == 23
    assert node.next is None


def test_remove_on_list_middle():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    result = ll.remove(1)
    assert result.value == 2
    assert ll.length == 2
    assert ll.head.value == 1
    assert ll.tail.value == 3
    assert ll.tail.next is None


def test_reverse_empty_list_doesnt_raise_exception():
    ll = LinkedList(None)
    ll.reverse()


def test_convert_to_python_list():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    conversion_result = ll.convert_to_python_list()
    assert len(conversion_result) == 3
    assert conversion_result == [1, 2, 3]


def test_reverse_list_with_three_elements():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    ll.reverse()
    assert ll.length == 3
    assert ll.convert_to_python_list() == [3, 2, 1]


def test_find_middle_node_list_with_three_elements():
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    node = ll.find_middle_node()
    assert node.value == 2


def test_find_middle_node_list_with_two_elements():
    ll = LinkedList(1)
    ll.append(2)
    node = ll.find_middle_node()
    assert node.value == 2
