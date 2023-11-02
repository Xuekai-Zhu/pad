def solution():
    red_candles = 45
    red_ratio = 5
    blue_ratio = 3
    
    # Calculate the total ratio (red_ratio + blue_ratio)
    total_ratio = red_ratio + blue_ratio

    # Calculate the fraction of the total that the red candles make up
    red_fraction = red_ratio / total_ratio

    # Calculate the total number of candles
    total_candles = red_candles / red_fraction

    # Calculate the number of blue candles
    blue_candles = total_candles - red_candles
    result = blue_candles
    return result

print(solution())