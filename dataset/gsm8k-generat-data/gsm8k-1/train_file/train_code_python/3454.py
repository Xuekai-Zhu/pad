def solution():
    """Sunny bakes 8 cakes. Then she gives away 2 cakes. Sunny wants to put candles on the remaining cakes. If she puts 6 candles on each cake, how many candles will she use in total?"""
    initial_cakes = 8
    given_away_cakes = 2
    remaining_cakes = initial_cakes - given_away_cakes
    candles_per_cake = 6
    total_candles = remaining_cakes * candles_per_cake
    result = total_candles
    return result

print(solution())