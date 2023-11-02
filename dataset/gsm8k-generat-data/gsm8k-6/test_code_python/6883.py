def solution():
    # Calculate the cost of replacing John's VHS with DVDs
    VHS_trade_in = 100 * 2  # John can trade in his VHS for $2 each, and he has 100 movies
    DVDs_cost = 100 * 10  # John needs to buy 100 DVDs, and they cost $10 each
    total_cost = DVDs_cost - VHS_trade_in  # John gets $2 for each VHS he trades in, so he only needs to pay $8 per DVD
    result = total_cost
    return result

print(solution())