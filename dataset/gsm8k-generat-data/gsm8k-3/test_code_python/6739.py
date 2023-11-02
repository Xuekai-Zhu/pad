def solution():
    """Ethan makes beeswax candles. For each candle, he uses 8 ounces of beeswax and 1 ounce of coconut oil. If he makes three less than 10 candles, what will be the combined weight of the candles in ounces?"""
    # Define the amount of beeswax and coconut oil needed for one candle
    BEESWAX_PER_CANDLE = 8
    COCONUT_OIL_PER_CANDLE = 1

    # Calculate the total number of candles Ethan makes
    total_candles = 10 - 3

    # Calculate the total amount of beeswax and coconut oil used
    total_beeswax = BEESWAX_PER_CANDLE * total_candles
    total_coconut_oil = COCONUT_OIL_PER_CANDLE * total_candles

    # Calculate the combined weight of the candles in ounces
    combined_weight = total_beeswax + total_coconut_oil

    # Display the combined weight
    result = combined_weight
    return result

print(solution())