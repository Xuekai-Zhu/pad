def solution():
    num_shares = 20
    initial_price = 3
    num_sold = 10
    sold_price = 4

    # Calculate the total cost of all shares
    total_cost = num_shares * initial_price

    # Calculate the total revenue from selling some of the shares
    total_revenue = num_sold * sold_price

    # Calculate the total value of the remaining shares after doubling in price
    remaining_shares = num_shares - num_sold
    remaining_value = remaining_shares * (initial_price * 2)

    # Calculate the total profit made
    total_profit = total_revenue + remaining_value - total_cost
    result = total_profit
    return result

print(solution())