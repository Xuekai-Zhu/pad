def solution():
    """Ethan makes beeswax candles. For each candle, he uses 8 ounces of beeswax and 1 ounce of coconut oil. If he makes three less than 10 candles, what will be the combined weight of the candles in ounces?"""
    candles = 10 - 3
    beeswax_weight = 8 * candles
    coconut_oil_weight = 1 * candles
    total_weight = beeswax_weight + coconut_oil_weight
    result = total_weight
    return result

print(solution())