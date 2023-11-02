def solution():
    
    total_cupcakes = 24
    half_cupcakes = total_cupcakes / 2
    one_candle_cupcakes = half_cupcakes
    two_candles_cupcakes = half_cupcakes

    total_candles = one_candle_cupcakes + (2 * two_candles_cupcakes)
    additional_candles = total_candles - 30

    result = additional_candles
    return result

print(solution())