def solution():
    
    total_cupcakes = 24
    total_candles = 30
    half_cupcakes = total_cupcakes / 2
    candles_for_half1 = half_cupcakes
    candles_for_half2 = half_cupcakes * 2
    candles_needed = candles_for_half1 + candles_for_half2 - total_candles
    result = candles_needed
    return result

print(solution())