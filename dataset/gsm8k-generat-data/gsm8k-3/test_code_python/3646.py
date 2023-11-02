def solution():
    """Barney's grocery store sold out all of its items at the beginning of the pandemic, so they ordered extra items to restock the shelves. However, they ended up ordering far too much and have to keep the leftover items in the storeroom. If they ordered 4458 items, sold another 1561 items that day, and have 575 items in the storeroom, how many items do they have left in the whole store?"""
    # Calculate the total number of items the store had initially
    total_items = 4458 + 575

    # Subtract the number of items sold that day
    total_items_sold = 1561
    items_left = total_items - total_items_sold

    # Display the number of items left in the store
    result = items_left
    return result

print(solution())