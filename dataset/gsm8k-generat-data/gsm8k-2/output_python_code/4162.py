def solution():
    """Tom buys 20 shares of a stock that costs $3 each. He sells 10 of those shares for $4 each. The rest of the shares end up doubling in value. How much profit does he make?"""
    shares_bought = 20
    cost_per_share = 3
    shares_sold = 10
    sell_price = 4
    remaining_shares = shares_bought - shares_sold
    remaining_shares_value = (remaining_shares * cost_per_share) * 2
    total_profit = (shares_sold * sell_price) + remaining_shares_value - (shares_bought * cost_per_share)
    result = total_profit
    return result

print(solution())