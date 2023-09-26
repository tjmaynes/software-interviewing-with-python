from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic, List

T = TypeVar('T')

@dataclass
class SinglyLinkedListNode(Generic[T]):
    value: T
    next: SinglyLinkedListNode[T] | None = None

class MySinglyLinkedList(Generic[T]):
    def __init__(self, *values: T) -> None:
        self.__head: SinglyLinkedListNode[T] | None = None
        self.__tail: SinglyLinkedListNode[T] | None = self.__head
        self.__length = 0

        for value in values:
            self.append(value)

    def append(self, value: T) -> None:
        if self.__length == 0:
            self.__head = SinglyLinkedListNode(value)
            self.__tail = self.__head
        else:
            new_node: SinglyLinkedListNode[T] = SinglyLinkedListNode(value)
            if self.__tail is not None:
                self.__tail.next = new_node
                self.__tail = new_node
        self.__length += 1

    def prepend(self, value: T) -> None:
        if self.__length == 0:
            self.__head = SinglyLinkedListNode(value)
        else:
            new_node = SinglyLinkedListNode(value, self.__head)
            self.__head = new_node
        self.__length += 1

    def insert(self, value: T, index: int) -> None:
        new_node = SinglyLinkedListNode(value)
        prev_node = self.__traverse_to_index(index)

        if index == 0:
            new_node.next = prev_node
            self.__head = new_node
        elif prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node

        if index == self.__length:
            self.__tail = new_node

        self.__length += 1

    def remove(self, value: T) -> None:
        if self.__head is not None and self.__head.value != value:
            prev_node = self.__head

            while prev_node.next is not None:
                if prev_node.next is not None:
                    if prev_node.next.value == value:
                        break
                prev_node = prev_node.next

            if prev_node is not None and prev_node.next is not None:
                prev_node.next = prev_node.next.next
            else:
                raise Exception(
                    "Value '{}' not found in SinglyLinkedList".format(value))
        elif self.__head is not None:
            self.__head = self.__head.next

        self.__length -= 1

    def __traverse_to_index(self, index: int) -> SinglyLinkedListNode[T] | None:
        curr = self.__head
        for i in range(index - 1):
            if curr is not None:
                curr = curr.next
        return curr

    def size(self) -> int:
        return self.__length

    def to_list(self) -> List[T]:
        if self.__length == 0:
            return []

        result = []
        curr = self.__head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return result