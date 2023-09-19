from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T')

@dataclass
class SinglyLinkedListNode(Generic[T]):
    value: T | None = None
    next: SinglyLinkedListNode[T] | None = None

class MySinglyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.__head: SinglyLinkedListNode[T] = SinglyLinkedListNode()
        self.__tail = self.__head
        self.__length = 1

    def size(self) -> int:
        return self.__length