def solution():
    
    num_cakes = 8
    num_given_away = 2
    num_remaining = num_cakes - num_given_away
    num_candles_per_cake = 6
    total_num_candles = num_remaining * num_candles_per_cake
    result = total_num_candles
    return result

print(solution())