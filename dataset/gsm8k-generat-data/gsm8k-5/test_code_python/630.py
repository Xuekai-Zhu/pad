def solution():
    red_to_blue_ratio = 5/3  # The ratio of red to blue candles is 5:3
    num_red_candles = 45  # Avianna had 45 red candles

    # Calculate the total number of candles Avianna had
    total_candles = num_red_candles / (5/3)

    # Calculate the number of blue candles Avianna had
    num_blue_candles = total_candles - num_red_candles
    result = num_blue_candles
    return result

print(solution())