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

    def test_conjured_item_quality(self):
        # quality of conjured items shall decrease twice as fast
        initial_quality = 8
        item = Item("perfect line of code", 12, initial_quality, "conjured")

        gr = GildedRose([item])
        gr.update_quality()

        self.assertEqual(initial_quality-2, item.quality)

    def test_expired_conjured_item_quality(self):
        # quality of conjured items shall decrease twice as fast
        initial_quality = 34
        item = Item("perfect line of code", 0, initial_quality, item_type='conjured')

        gr = GildedRose([item])
        gr.update_quality()

        self.assertEqual(initial_quality-4, item.quality)

class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sample_items_args = [
            ('bar', 124, 34),
            ('baz', 3, 2),
            ('conjured spoon', 7, 42, 'conjured'),
            ('Fake conjured item', 7, 42, 'conjured')
        ]

    def test_item_type(self):
        for item_args in self.sample_items_args:
            item = Item(*item_args)

            self.assertTrue(hasattr(item, 'item_type'))

            exp_type = 'conjured' if len(item_args) > 3 and 'conjured' in item_args[-1] else 'miscellaneous'
            self.assertEqual(exp_type, item.item_type)

    def test_quality_rate(self):
        for item_args in self.sample_items_args:
            item = Item(*item_args)

            self.assertTrue(hasattr(item, 'quality_rate'))

            if 'conjured' in item.item_type:
                self.assertEqual(Item.default_quality_rate * 2, item.quality_rate)
            else:
                self.assertEqual(Item.default_quality_rate, item.quality_rate)


if __name__ == '__main__':
    unittest.main()
