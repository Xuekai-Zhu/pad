def solution():
    """Stephanie is decorating 24 cupcakes for a birthday party, but she needs more candles. She currently has a total of 30 candles. She wants to decorate half of the cupcakes with 1 candle each and the other half of the cupcakes with 2 candles each. How many additional candles does Stephanie need to complete the cupcakes?"""
    total_cupcakes = 24
    half_cupcakes = total_cupcakes / 2
    one_candle_cupcakes = half_cupcakes
    two_candles_cupcakes = half_cupcakes

    total_candles = one_candle_cupcakes + (2 * two_candles_cupcakes)
    additional_candles = total_candles - 30

    result = additional_candles
    return result

print(solution())