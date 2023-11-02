def solution():
    # Calculate the cost of the burnt cupcakes
    burnt_cost = 0.75 * 24 * 2

    # Calculate the cost of the cupcakes Prudence ate
    eaten_cost = 0.75 * (5 + 4)

    # Calculate the cost of the 2 dozen cupcakes that came out perfectly
    perfect_cost = 0.75 * 24 * 2

    # Calculate the total cost of making the cupcakes
    total_cost = burnt_cost + eaten_cost + perfect_cost

    # Calculate the revenue from selling the remaining cupcakes
    remaining_revenue = (24 - 5 - 4) * 2

    # Calculate the net profit
    net_profit = remaining_revenue - total_cost
    result = net_profit
    return result

print(solution())