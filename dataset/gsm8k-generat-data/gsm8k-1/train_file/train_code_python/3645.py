def solution():
    """Barney's grocery store sold out all of its items at the beginning of the pandemic, so they ordered extra items to restock the shelves. However, they ended up ordering far too much and have to keep the leftover items in the storeroom. If they ordered 4458 items, sold another 1561 items that day, and have 575 items in the storeroom, how many items do they have left in the whole store?"""
    items_ordered = 4458
    items_sold = 1561
    items_in_storeroom = 575
    total_items = items_ordered - items_sold + items_in_storeroom
    result = total_items
    return result

print(solution())