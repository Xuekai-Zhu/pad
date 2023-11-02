def solution():
    """Sunny bakes 8 cakes. Then she gives away 2 cakes. Sunny wants to put candles on the remaining cakes. If she puts 6 candles on each cake, how many candles will she use in total?"""
    num_cakes = 8
    num_given_away = 2
    num_remaining = num_cakes - num_given_away
    num_candles_per_cake = 6
    total_num_candles = num_remaining * num_candles_per_cake
    result = total_num_candles
    return result

print(solution())