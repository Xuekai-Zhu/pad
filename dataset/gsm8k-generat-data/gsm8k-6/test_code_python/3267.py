def solution():
    # Calculate the total number of candles used
    total_candles = 79  # one candle for each year

    # Calculate the number of blue candles used
    blue_candles = total_candles - 27 - 14  # the rest are blue

    result = blue_candles
    return result

print(solution())