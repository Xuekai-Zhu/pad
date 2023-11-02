def solution():
    """John decides to replace all his VHS with DVDs. He can trade in his VHS for $2 each and then buy the DVDs for $10 each. If he has 100 movies, how much does it cost to replace his movies?"""
    num_movies = 100
    trade_in_value = 2
    dvd_cost = 10
    total_trade_in_value = num_movies * trade_in_value
    total_dvd_cost = (num_movies * dvd_cost) - total_trade_in_value
    result = total_dvd_cost
    return result

print(solution())