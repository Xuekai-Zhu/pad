def solution():
    num_ducks = 30
    duck_cost = 10
    duck_weight = 4
    duck_price_per_lb = 5

    # Calculate the total cost of all ducks
    total_cost = num_ducks * duck_cost

    # Calculate the total weight of all ducks
    total_weight = num_ducks * duck_weight

    # Calculate the total revenue from selling all ducks
    total_revenue = total_weight * duck_price_per_lb

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())