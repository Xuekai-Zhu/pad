def solution():
    total_cupcakes = 24
    total_candles = 30
    cupcakes_with_one_candle = total_cupcakes / 2
    cupcakes_with_two_candles = total_cupcakes - cupcakes_with_one_candle
    candles_needed = cupcakes_with_two_candles - total_candles
    result = candles_needed
    return result

print(solution())