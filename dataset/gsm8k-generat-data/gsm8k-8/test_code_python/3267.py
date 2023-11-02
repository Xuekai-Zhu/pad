def solution():
    # Calculate the total number of candles used
    total_candles = 79

    # Subtract the number of yellow and red candles from the total to find the number of blue candles
    blue_candles = total_candles - 27 - 14

    result = blue_candles
    return result

print(solution())