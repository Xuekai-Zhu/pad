def solution():
    
    items_ordered = 4458
    items_sold = 1561
    items_in_storeroom = 575
    total_items = items_ordered - items_sold + items_in_storeroom
    result = total_items
    return result

print(solution())