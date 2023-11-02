def solution():
    # Calculate the initial cost of the shares
    initial_cost = 20 * 3

    # Calculate the revenue from selling 10 of the shares
    revenue = 10 * 4

    # Calculate the remaining shares and their new value
    remaining_shares = 20 - 10
    remaining_value = 2 * 3

    # Calculate the total revenue from the remaining shares
    remaining_revenue = remaining_shares * remaining_value

    # Calculate the total profit
    total_profit = revenue + remaining_revenue - initial_cost
    result = total_profit
    return result

print(solution())