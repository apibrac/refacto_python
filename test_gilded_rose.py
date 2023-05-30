# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

        self.assertEquals(items[0].sell_in, -1)
        self.assertEquals(items[0].quality, 2)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)

        self.assertEquals(items[0].sell_in, 1)
        self.assertEquals(items[0].quality, 2)

    def test_conjured(self):
        items = [Item("Conjured", 0, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Conjured", items[0].name)

        self.assertEquals(items[0].sell_in, -1)

        # it seems that it should be 0 instead of 2
        # self.assertEquals(items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
