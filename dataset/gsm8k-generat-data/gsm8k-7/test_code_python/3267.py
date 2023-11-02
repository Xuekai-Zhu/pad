def solution():
    grandfather_age = 79
    yellow_candles = 27
    red_candles = 14

    # Calculate the total number of candles on the cake
    total_candles = grandfather_age

    # Calculate the number of blue candles
    blue_candles = total_candles - yellow_candles - red_candles
    result = blue_candles
    return result

print(solution())