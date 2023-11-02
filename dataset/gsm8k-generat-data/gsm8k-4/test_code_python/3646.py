def solution():
    """Barney's grocery store sold out all of its items at the beginning of the pandemic, so they ordered extra items to restock the shelves. However, they ended up ordering far too much and have to keep the leftover items in the storeroom. If they ordered 4458 items, sold another 1561 items that day, and have 575 items in the storeroom, how many items do they have left in the whole store?"""
    # Define the initial number of items
    initial_items = 4458

    # Calculate the number of items sold
    sold_items = 1561

    # Calculate the number of items left in the store
    remaining_items = initial_items - sold_items + 575

    # return the result
    result = remaining_items
    return result

print(solution())