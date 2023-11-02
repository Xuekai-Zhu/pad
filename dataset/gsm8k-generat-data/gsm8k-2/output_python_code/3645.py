def solution():
    """Barney's grocery store sold out all of its items at the beginning of the pandemic, so they ordered extra items to restock the shelves. However, they ended up ordering far too much and have to keep the leftover items in the storeroom. If they ordered 4458 items, sold another 1561 items that day, and have 575 items in the storeroom, how many items do they have left in the whole store?"""
    ordered_items = 4458
    sold_items = 1561
    storeroom_items = 575
    remaining_items = ordered_items - sold_items - storeroom_items
    result = remaining_items
    return result

print(solution())