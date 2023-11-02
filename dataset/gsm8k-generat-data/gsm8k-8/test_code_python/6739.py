def solution():
    # Define the amount of ingredients per candle
    beeswax_per_candle = 8
    coconut_oil_per_candle = 1

    # Calculate the total amount of ingredients for the number of candles Ethan makes
    num_candles = 10 - 3
    total_beeswax = beeswax_per_candle * num_candles
    total_coconut_oil = coconut_oil_per_candle * num_candles

    # Calculate the combined weight in ounces of the candles
    combined_weight = total_beeswax + total_coconut_oil
    result = combined_weight
    return result

print(solution())