def solution():
    # Calculate the amount of money John can get from trading in his VHS tapes
    vhs_trade_in = 2 * 100

    # Calculate the cost of buying 100 DVDs
    dvd_cost = 10 * 100

    # Calculate the total cost of replacing the VHS tapes with DVDs
    total_cost = dvd_cost - vhs_trade_in
    result = total_cost
    return result

print(solution())