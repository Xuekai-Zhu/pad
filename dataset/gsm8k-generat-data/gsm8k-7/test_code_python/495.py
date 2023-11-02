def solution():
    num_pretzels = 64
    num_goldfish = 4 * num_pretzels
    num_suckers = 32
    num_kids = 16

    # Calculate the total number of items in each baggie
    total_items = num_pretzels + num_goldfish + num_suckers
    items_per_baggie = total_items / num_kids

    result = items_per_baggie
    return result

print(solution())