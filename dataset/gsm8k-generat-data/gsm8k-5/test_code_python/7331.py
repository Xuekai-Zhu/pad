def solution():
    big_bottle_size = 30  # Big bottles hold 30 ounces of mango juice
    big_bottle_cost = 2700  # Big bottles cost 2700 pesetas each
    small_bottle_size = 6  # Small bottles hold 6 ounces of mango juice
    small_bottle_cost = 600  # Small bottles cost 600 pesetas each

    # Calculate the cost of buying the same volume of juice in small bottles
    num_small_bottles = big_bottle_size / small_bottle_size  # The number of small bottles needed to match the size of a big bottle
    total_small_bottle_cost = num_small_bottles * small_bottle_cost  # The total cost of buying the small bottles

    # Calculate the amount saved by buying a big bottle instead of smaller bottles
    amount_saved = total_small_bottle_cost - big_bottle_cost
    result = amount_saved
    return result

print(solution())