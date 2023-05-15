# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            # update quality
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.decrease_quality()
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1

            # update sell_in
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            # re-update quality for expired items
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.decrease_quality()
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:

    default_quality_rate = -1

    def __init__(self, name, sell_in, quality, item_type='miscellaneous'):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.item_type = str(item_type).lower()

        self.set_quality_rate()

    def __repr__(self):
        return "Item(name=%s, sell_in=%s, quality=%s, item_type=%s)" % (self.name, self.sell_in, self.quality, self.item_type)

    def set_quality_rate(self):
        if 'conjured' in self.item_type:
            self.quality_rate = self.default_quality_rate * 2
        else:
            self.quality_rate = self.default_quality_rate
    def decrease_quality(self):
        self.quality += self.quality_rate