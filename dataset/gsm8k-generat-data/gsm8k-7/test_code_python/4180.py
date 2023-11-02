def solution():
    bar_cost = 8.0
    months_per_bar = 2
    num_bars_per_year = 12

    # Calculate the total cost of one year's supply of soap
    cost_per_year = num_bars_per_year * bar_cost

    # Calculate the number of bars of soap needed for one year
    num_bars_per_year = 12 / months_per_bar

    # Calculate the total cost of all bars of soap needed for one year
    total_cost = num_bars_per_year * bar_cost
    result = total_cost
    return result

print(solution())