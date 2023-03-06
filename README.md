# Gilded Rose

This is the Gilded Rose kata in JavaScript with Jest

## Test description

Hi and welcome to the team of the Gilded Rose. As you know, we are a small inn in a prime location of a
prominent city ran by a friendly innkeeper named Allison. We also buy and sell only the finest goods.
Unfortunately, our goods are constantly degrading in quality as they approach their expiration date. We
have build a system that updates our inventory for us. It was developed by a no-nonsense kind of guy named
Leeroy, who has now moved on to new adventures. Your task is to add a new feature to our system so that
we can start selling a new category of items. But first an introduction to our system:

    - All items have a SellIn value, which denotes the number of days we have left before the expiration date
    - All items have a Quality value, which denotes how valuable the item is
    - At the end of each day our system lowers both values for every item

Pretty simple, right? Well this is where it gets interesting:

    - Once the expiration date is reached, Quality degrades twice as fast
    - The Quality of an item is never negative
    - "Aged Brie" actually increases in Quality the older it gets
    - The Quality of an item is never more than 50
    - "Sulfuras", being a legendary item, doesn't have a expiration date or decreases in Quality
    - "Backstage passes", like Aged Brie, increases in Quality as its SellIn value lowers;
    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert

We have recently signed with a supplier of conjured items. This requires an update to our system:

    - "Conjured" items degrade in Quality twice as fast as normal items

Feel free to make any changes and add any new code as long as everything
still works correctly.

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a
legendary item and as such its Quality is 80 and it never alters.
