def solution():
    """Ethan makes beeswax candles. For each candle, he uses 8 ounces of beeswax and 1 ounce of coconut oil. If he makes three less than 10 candles, what will be the combined weight of the candles in ounces?"""
    # Define the amount of beeswax and coconut oil used per candle
    BEESWAX_PER_CANDLE = 8
    COCONUT_OIL_PER_CANDLE = 1

    # Define the number of candles Ethan makes
    num_candles = 10 - 3

    # Calculate the total weight of beeswax and coconut oil used
    total_beeswax = BEESWAX_PER_CANDLE * num_candles
    total_coconut_oil = COCONUT_OIL_PER_CANDLE * num_candles

    # Calculate the combined weight of the candles
    combined_weight = total_beeswax + total_coconut_oil

    # return the result
    result = combined_weight
    return result

print(solution())