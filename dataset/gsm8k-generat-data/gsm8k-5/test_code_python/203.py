def solution():
    soft_drinks_cost = 4  # Each soft drink costs $4
    total_soft_drinks_cost = 2 * soft_drinks_cost  # Benny bought 2 soft drinks
    total_spent = 28  # Benny spent a total of $28
    candy_bars_count = 5  # Benny bought 5 candy bars

    # Calculate the cost of the candy bars
    candy_bars_cost = (total_spent - total_soft_drinks_cost) / candy_bars_count
    result = candy_bars_cost
    return result

print(solution())