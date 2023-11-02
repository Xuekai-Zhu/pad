def solution():
    # Define the ratio of red candles to blue candles
    red_to_blue_ratio = 5/3

    # Calculate the total number of candles
    total_candles = 45 / (5/3 + 1)

    # Calculate the number of blue candles
    blue_candles = total_candles * (1/3)

    result = blue_candles
    return result

print(solution())