def solution():
    pretzels = 64
    goldfish = 4 * pretzels
    suckers = 32
    num_kids = 16

    # Calculate total number of items
    total_items = pretzels + goldfish + suckers

    # Divide total items by number of bags
    items_per_bag = total_items / num_kids
    result = items_per_bag
    return result

print(solution())