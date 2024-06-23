from typing import Optional


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
            return
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def convert_to_python_list(self) -> list:
        list_representation = []
        temp = self.head
        while temp is not None:
            list_representation.append(temp.value)
            temp = temp.next
        return list_representation

    @property
    def is_empty(self) -> bool:
        return self.head is None

    def append(self, value) -> bool:
        """
        Time Complexity: O(1)
        """
        new_node = Node(value)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Optional[Node]:
        """
        Time Complexity: O(N)
        """
        if self.is_empty:
            return None
        temp = self.head
        previous = self.head
        while temp.next is not None:
            previous = temp
            temp = temp.next
        self.tail = previous
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def preppend(self, value) -> bool:
        """
        Time complexity O(1)
        """
        new_node = Node(value)
        if self.is_empty:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Optional[Node]:
        """
        Time complexity O(1)
        """
        if self.is_empty:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.is_empty:
            self.tail = None
        return temp

    def get(self, index) -> Optional[Node]:
        """
        Time complexity O(N)
        """
        if index < 0 or index >= self.length:
            return None
        if self.is_empty:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value) -> bool:
        """
        Time complexity O(N)
        """
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

    def insert(self, index, value) -> bool:
        """
        Time complexity O(N)
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.preppend(value)
        if index == self.length:
            return self.append(value)
        # inserting in the middle
        new_node = Node(value)
        previous_node = self.get(index - 1)
        new_node.next = previous_node.next
        previous_node.next = new_node
        self.length += 1
        return True

    def remove(self, index) -> Optional[Node]:
        """
        Time complexity O(N)
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        # removing from the middle
        previous_node = self.get(index - 1)
        node_to_remove = previous_node.next
        previous_node.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

    def reverse(self):
        """
        Time complexity O(N)
        """
        if self.is_empty:
            return
        current_node = self.head.next
        previous_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.tail = self.head
        self.tail.next = None
        self.head = previous_node

    def find_middle_node(self):
        """
        Time complexity O(N)
        """
        if self.head is None:
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
