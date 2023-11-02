def solution():
    initial_order = 4458
    sold_items = 1561
    storeroom_items = 575

    # Calculate the total number of items in the store before selling
    total_items = initial_order + storeroom_items

    # Calculate the total number of items left in the store after selling
    remaining_items = total_items - sold_items
    result = remaining_items
    return result

print(solution())