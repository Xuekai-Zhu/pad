def solution():
    
    red_candles_ratio = 5
    blue_candles_ratio = 3
    total_candles_ratio = red_candles_ratio + blue_candles_ratio
    red_candles_count = 45
    red_candles_unit = red_candles_count / red_candles_ratio
    blue_candles_count = blue_candles_ratio * red_candles_unit
    result = blue_candles_count
    return result

print(solution())