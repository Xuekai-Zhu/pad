def solution():
    big_bottle_volume = 30
    big_bottle_cost = 2700
    small_bottle_volume = 6
    small_bottle_cost = 600
    required_volume = 30

    # Calculate the total cost of buying small bottles for the required volume
    num_small_bottles = required_volume / small_bottle_volume
    total_small_bottle_cost = num_small_bottles * small_bottle_cost

    # Calculate the cost of buying one big bottle for the required volume
    num_big_bottles = required_volume / big_bottle_volume
    total_big_bottle_cost = num_big_bottles * big_bottle_cost

    # Calculate the pesetas saved by buying a big bottle instead of smaller bottles for the same volume
    pesetas_saved = total_small_bottle_cost - total_big_bottle_cost
    result = pesetas_saved
    return result

print(solution())