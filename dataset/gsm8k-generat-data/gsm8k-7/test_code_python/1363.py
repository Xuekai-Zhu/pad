def solution():
    cost_per_cupcake = 0.75
    num_burnt_dozen = 2
    num_perfect_dozen = 2
    num_eaten_initially = 5
    num_eaten_later = 4
    price_per_cupcake = 2.0

    # Calculate the total number of cupcakes made
    total_cupcakes_made = (num_burnt_dozen + num_perfect_dozen) * 12

    # Calculate the total cost of all ingredients
    total_cost = total_cupcakes_made * cost_per_cupcake

    # Calculate the total number of cupcakes eaten
    total_eaten = num_eaten_initially + num_eaten_later

    # Calculate the total revenue from selling the remaining cupcakes
    total_revenue = (total_cupcakes_made - total_eaten) * price_per_cupcake

    # Calculate the net profit
    net_profit = total_revenue - total_cost
    result = net_profit
    return result

print(solution())