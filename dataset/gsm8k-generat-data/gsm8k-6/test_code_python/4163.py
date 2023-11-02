def solution():
    # Calculate the total cost of the shares
    total_cost = 20 * 3

    # Calculate the total revenue from selling the 10 shares
    revenue = 10 * 4

    # Calculate the remaining shares' value after doubling
    remaining_shares_value = (20 - 10) * 3 * 2

    # Calculate the total profit
    profit = revenue + remaining_shares_value - total_cost
    result = profit
    return result

print(solution())