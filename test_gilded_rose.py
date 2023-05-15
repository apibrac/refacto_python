# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        exp_name = "foo"
        items = [Item(exp_name, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(exp_name, items[0].name)

        
if __name__ == '__main__':
    unittest.main()
