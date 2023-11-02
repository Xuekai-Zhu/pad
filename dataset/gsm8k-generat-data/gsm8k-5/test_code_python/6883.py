def solution():
    num_movies = 100  # John has 100 movies to replace
    vhs_trade_in = 2  # John can trade in each VHS for $2
    dvd_cost = 10  # John needs to buy each DVD for $10

    # Calculate the cost of replacing all the movies
    cost_trade_in = num_movies * vhs_trade_in
    cost_dvds = num_movies * dvd_cost
    total_cost = cost_dvds - cost_trade_in  # John gets a discount by trading in his VHS

    result = total_cost
    return result

print(solution())