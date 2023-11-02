def solution():
    # Calculate the cost of buying the same volume of juice with small bottles
    small_bottle_cost = 6 * 5 * 600  # 5 small bottles needed for 30 ounces
    # Calculate the cost of buying a big bottle
    big_bottle_cost = 2700
    # Calculate the pesetas saved by buying a big bottle instead of small bottles
    pesetas_saved = small_bottle_cost - big_bottle_cost
    result = pesetas_saved
    return result

print(solution())