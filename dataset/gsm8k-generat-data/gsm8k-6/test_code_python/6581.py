def solution():
    # Calculate Andy's profit for each cake
    cost_per_cake = 12/2 + 1  # $12 for 2 cakes, $1 packaging cost per cake
    profit_per_cake = 15 - cost_per_cake  # Andy sells each cake for $15
    result = profit_per_cake
    return result

print(solution())