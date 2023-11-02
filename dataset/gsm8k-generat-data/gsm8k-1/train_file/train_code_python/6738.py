def solution():
    """Ethan makes beeswax candles. For each candle, he uses 8 ounces of beeswax and 1 ounce of coconut oil. If he makes three less than 10 candles, what will be the combined weight of the candles in ounces?"""
    beeswax_per_candle = 8
    coconut_oil_per_candle = 1
    candles_made = 10 - 3
    total_weight = (beeswax_per_candle + coconut_oil_per_candle) * candles_made
    result = total_weight
    return result

print(solution())