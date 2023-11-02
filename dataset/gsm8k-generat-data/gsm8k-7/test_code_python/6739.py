def solution():
    beeswax_per_candle = 8
    coconut_oil_per_candle = 1
    num_candles = 9  # Ethan makes three less than 10 candles

    # Calculate the total weight of the beeswax needed for all candles
    total_beeswax = beeswax_per_candle * num_candles

    # Calculate the total weight of the coconut oil needed for all candles
    total_coconut_oil = coconut_oil_per_candle * num_candles

    # Calculate the combined weight of all candles
    total_weight = total_beeswax + total_coconut_oil
    result = total_weight
    return result

print(solution())