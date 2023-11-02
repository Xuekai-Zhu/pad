def solution():
    
    num_movies = 100
    vhs_trade_in = 2
    dvd_cost = 10
    total_cost = (num_movies * dvd_cost) - (num_movies * vhs_trade_in)
    result = total_cost
    return result

print(solution())