def solution():
    shares = 20  # Tom buys 20 shares of a stock
    initial_price = 3  # The initial price of each share is $3

    # Calculate the total cost of buying the shares
    total_cost = shares * initial_price

    # Calculate the amount earned from selling 10 shares at $4 each
    amount_earned = 10 * 4

    # Calculate the remaining shares' new value after doubling in price
    remaining_shares = shares - 10
    new_price = initial_price * 2
    remaining_value = remaining_shares * new_price

    # Calculate Tom's total profit
    total_profit = (amount_earned + remaining_value) - total_cost
    result = total_profit
    return result

print(solution())