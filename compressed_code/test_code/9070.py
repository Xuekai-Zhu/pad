def solution():
    
    num_shares = 20
    share_cost = 3
    shares_sold = 10
    shares_remaining = num_shares - shares_sold
    shares_remaining_value = (share_cost * shares_remaining) * 2
    total_cost = num_shares * share_cost
    total_earnings = (shares_sold * 4) + shares_remaining_value
    profit = total_earnings - total_cost
    result = profit
    return result

print(solution())