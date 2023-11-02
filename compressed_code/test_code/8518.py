def solution():
    
    initial_cakes = 8
    given_away_cakes = 2
    remaining_cakes = initial_cakes - given_away_cakes
    candles_per_cake = 6
    total_candles = remaining_cakes * candles_per_cake
    result = total_candles
    return result

print(solution())