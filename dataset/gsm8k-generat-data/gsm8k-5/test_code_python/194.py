def solution():
    cost_polo_shirts = 3 * 26  # Mr. Grey purchased 3 polo shirts for $26 each
    cost_necklaces = 2 * 83  # Mr. Grey purchased 2 necklaces for $83 each
    cost_computer_game = 90  # Mr. Grey purchased 1 computer game for $90
    total_cost = cost_polo_shirts + cost_necklaces + cost_computer_game  # Total cost before rebate
    total_cost -= 12  # Deduct $12 rebate from the total cost
    result = total_cost
    return result

print(solution())