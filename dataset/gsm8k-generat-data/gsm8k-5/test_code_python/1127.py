def solution():
    useful_items_percent = 0.2  # 20% of the items are useful
    valuable_items_percent = 0.1  # 10% of the items are valuable heirlooms
    junk_items_percent = 0.7  # 70% of the items are junk
    useful_items = 8  # Marcus's attic has 8 useful items

    # Calculate the total number of items in the attic
    total_items = useful_items / useful_items_percent

    # Calculate the number of junk items in the attic
    junk_items = total_items * junk_items_percent
    result = junk_items
    return result

print(solution())