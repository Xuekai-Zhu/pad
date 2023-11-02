def solution():
    num_movies = 100
    vhs_trade_in = 2
    dvd_cost = 10

    # Calculate the amount of money John gets from trading in his VHS
    trade_in_amount = num_movies * vhs_trade_in

    # Calculate the total cost for buying all the DVDs
    dvd_cost_total = num_movies * dvd_cost

    # Calculate the final cost after deducting the trade-in amount
    final_cost = dvd_cost_total - trade_in_amount
    result = final_cost
    return result

print(solution())