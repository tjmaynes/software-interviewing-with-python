from typing import TypeVar, Generic, List

T = TypeVar('T')

class MyArrayImpl(Generic[T]):
    def __init__(self, *items: T) -> None:
        self.__data = []
        for item in items:
            self.__data.append(item)

    def get_all(self) -> List[T]:
        return self.__data
 
    def index(self, item: T) -> int:
        # can also just use self.__data.index(item)
        for index, _item in enumerate(self.__data):
            if _item == item:
                return index
        return -1

    def push(self, item: T) -> None:
        if item not in self.__data:
            self.__data.append(item)

    def pop(self) -> None:
        if self.size() > 0:
            del self.__data[0]

    def delete(self, item: T) -> None:
        if self.index(item) != -1:
            self.__data.remove(item)

    def size(self) -> int:
        return len(self.__data)