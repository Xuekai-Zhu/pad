def solution():
    """John decides to replace all his VHS with DVDs. He can trade in his VHS for $2 each and then buy the DVDs for $10 each. If he has 100 movies, how much does it cost to replace his movies?"""
    num_movies = 100
    vhs_trade_in = 2
    dvd_cost = 10
    total_cost = (num_movies * dvd_cost) - (num_movies * vhs_trade_in)
    result = total_cost
    return result

print(solution())