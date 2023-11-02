def solution():
    num_soft_drinks = 2
    soft_drink_price = 4

    num_candy_bars = 5
    total_spent = 28

    # Calculate the total cost of all soft drinks
    total_soft_drink_cost = num_soft_drinks * soft_drink_price

    # Calculate the total cost of all candy bars
    total_candy_bar_cost = total_spent - total_soft_drink_cost

    # Calculate the cost of each candy bar
    cost_per_candy_bar = total_candy_bar_cost / num_candy_bars
    result = cost_per_candy_bar
    return result

print(solution())