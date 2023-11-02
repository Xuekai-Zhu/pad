def solution():
    # Calculate the total cost of the two soft drinks
    soft_drinks_cost = 2 * 4

    # Calculate the total cost of the candy bars
    candy_bars_cost = 28 - soft_drinks_cost

    # Calculate the cost of each candy bar
    cost_per_candy_bar = candy_bars_cost / 5
    result = cost_per_candy_bar
    return result

print(solution())