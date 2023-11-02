def solution():
    # Calculate the total cost of all the toys
    total_cost = 20 * 200

    # Calculate the number of toys James decides to sell
    num_to_sell = 0.8 * 200

    # Calculate the total revenue from selling these toys
    total_revenue = 30 * num_to_sell

    # Calculate James' profit
    profit = total_revenue - total_cost

    result = profit
    return result

print(solution())