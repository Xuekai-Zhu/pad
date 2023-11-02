def solution():
    # Calculate the total weight of the tomatoes
    total_weight = 20 * 3

    # Subtract the weight of the rotten tomatoes
    total_weight -= 3

    # Calculate the total revenue from selling the tomatoes
    total_revenue = total_weight * 6

    # Calculate the total cost of buying the crates
    total_cost = 330

    # Calculate Tommy's profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())