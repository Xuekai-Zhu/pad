def solution():
    # Define the cost of the soft drinks and the total amount spent
    soft_drink_cost = 4
    total_soft_drinks_cost = 2 * soft_drink_cost
    total_spent = 28

    # Calculate the total cost of the candy bars
    total_candy_bars_cost = total_spent - total_soft_drinks_cost

    # Calculate the cost of each candy bar
    candy_bar_cost = total_candy_bars_cost / 5
    result = candy_bar_cost
    return result

print(solution())