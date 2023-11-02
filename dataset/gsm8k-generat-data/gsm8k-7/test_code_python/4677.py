def solution():
    total_rolls_needed = 45
    rolls_sold_so_far = 1 + 10 + 6  # Rolls sold to grandmother, uncle, and neighbor
    rolls_left_to_sell = total_rolls_needed - rolls_sold_so_far
    result = rolls_left_to_sell
    return result

print(solution())