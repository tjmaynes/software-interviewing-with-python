# type: ignore
from data_structures.array import MyArrayImpl

import unittest

class TestMyArrayImpl(unittest.TestCase):
    def test_init_whenGivenDefaultItems_itShouldContainEmptyData(self):
        sut = MyArrayImpl(8, 9, 10)

        self.assertEqual(sut.get_all(), [8, 9, 10])

    def test_init_whenNotGivenDefaultItems_itShouldContainEmptyData(self):
        sut = MyArrayImpl()

        self.assertEqual(sut.get_all(), [])

    def test_index_whenItemExists_itShouldReturnItemIndex(self):
        sut = MyArrayImpl(10, 11, 12)

        actual = sut.index(12)

        self.assertEqual(actual, 2)

    def test_index_whenItemDoesNotExist_itShouldReturnNegativeOne(self):
        sut = MyArrayImpl(1, 2, 3)

        actual = sut.index(4)

        self.assertEqual(actual, -1)

    def test_push_whenGivenAnItem_itShouldAppendItemToBottomOfArray(self):
        sut = MyArrayImpl(11, 12)

        sut.push(10)

        self.assertEqual(sut.get_all(), [11, 12, 10])

    def test_push_whenGivenADuplicateItem_itShouldNotAddItemAgain(self):
        sut = MyArrayImpl(10, 11, 12)

        sut.push(10)

        self.assertEqual(sut.get_all(), [10, 11, 12])

    def test_pop_whenCalled_itShouldRemoveLastInsertedItem(self):
        sut = MyArrayImpl(8, 9, 10)

        sut.pop()

        self.assertEqual(sut.get_all(), [9, 10])

    def test_pop_whenArrayIsEmpty_itShouldDoNothing(self):
        sut = MyArrayImpl()

        sut.pop()

        self.assertEqual(sut.get_all(), [])

    def test_delete_whenGivenAnItem_itShouldRemoveItemFromArray(self):
        sut = MyArrayImpl(11, 12, 13)

        sut.delete(13)

        self.assertEqual(sut.get_all(), [11, 12])

    def test_delete_whenGivenAnNonExistentItem_itShouldDoNothing(self):
        sut = MyArrayImpl(10, 11, 12)

        sut.delete(44)

        self.assertEqual(sut.get_all(), [10, 11, 12])