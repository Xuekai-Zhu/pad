def solution():
    # Calculate the number of small bottles needed to hold 30 ounces of juice
    num_small_bottles = 30 / 6

    # Calculate the cost of buying small bottles
    small_bottle_cost = num_small_bottles * 600

    # Calculate the cost of buying a big bottle
    big_bottle_cost = 2700

    # Calculate the amount saved by buying a big bottle
    amount_saved = small_bottle_cost - big_bottle_cost
    result = amount_saved
    return result

print(solution())