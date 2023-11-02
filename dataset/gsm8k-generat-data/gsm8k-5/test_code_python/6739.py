def solution():
    ounces_per_candle = 8 + 1  # Ethan uses 8 ounces of beeswax and 1 ounce of coconut oil per candle
    num_candles = 10 - 3  # Ethan makes three less than 10 candles
    total_weight = ounces_per_candle * num_candles  # Calculate the total weight in ounces

    result = total_weight
    return result

print(solution())