# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in(self):
        items = [Item("foo", 3, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].sell_in)

    def test_quality_1(self):
        items = [Item("foo", 3, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_quality_2(self):
        items = [Item("foo", -1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_quality_1(self):
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_aged_brie_quality_2(self):
        items = [Item("Aged Brie", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_aged_brie_quality_3(self):
        items = [Item("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)

    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_conjured_quality(self):
        items = [Item("Conjured Mana Cake", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_conjured_sell_in(self):
        items = [Item("Conjured Dragon Blood", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_passes_1(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes_4(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 400)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
