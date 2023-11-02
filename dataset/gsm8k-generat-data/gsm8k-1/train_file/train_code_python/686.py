def solution():
    """Stephanie is decorating 24 cupcakes for a birthday party, but she needs more candles. She currently has a total of 30 candles. She wants to decorate half of the cupcakes with 1 candle each and the other half of the cupcakes with 2 candles each. How many additional candles does Stephanie need to complete the cupcakes?"""
    total_cupcakes = 24
    total_candles = 30
    half_cupcakes = total_cupcakes / 2
    candles_for_half1 = half_cupcakes
    candles_for_half2 = half_cupcakes * 2
    candles_needed = candles_for_half1 + candles_for_half2 - total_candles
    result = candles_needed
    return result

print(solution())