def solution():
    # Total items in the store
    total_items = 4458

    # Items sold that day
    items_sold = 1561

    # Items in the storeroom
    items_storeroom = 575

    # Calculate the remaining items in the store
    remaining_items = total_items - items_sold - items_storeroom
    result = remaining_items
    return result

print(solution())