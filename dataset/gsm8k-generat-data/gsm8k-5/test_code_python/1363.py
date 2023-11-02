def solution():
    cost_per_cupcake = 0.75  # Prudence spent $0.75 to make each cupcake
    burnt_cupcakes = 2 * 12  # Prudence burnt the first 2 dozen cupcakes, which is a total of 24 cupcakes
    perfect_cupcakes = 2 * 12  # Prudence made 2 dozen perfect cupcakes, which is a total of 24 cupcakes
    eaten_cupcakes = 5 + 4  # Prudence ate 5 cupcakes from the first batch and 4 from the second batch, which is a total of 9 cupcakes

    # Calculate the total cost of the cupcakes
    total_cost = (burnt_cupcakes + perfect_cupcakes - eaten_cupcakes) * cost_per_cupcake

    # Calculate the total revenue from selling the remaining cupcakes
    remaining_cupcakes = burnt_cupcakes + perfect_cupcakes - eaten_cupcakes
    revenue = remaining_cupcakes * 2.00

    # Calculate the net profit
    net_profit = revenue - total_cost
    result = net_profit
    return result

print(solution())