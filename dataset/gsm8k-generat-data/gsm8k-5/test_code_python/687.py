def solution():
    total_cupcakes = 24  # Stephanie is decorating 24 cupcakes
    total_candles = 30  # Stephanie currently has 30 candles

    # Calculate how many candles Stephanie needs for half of the cupcakes to have 1 candle each
    candles_half_1 = (total_cupcakes // 2)  

    # Calculate how many candles Stephanie needs for half of the cupcakes to have 2 candles each
    candles_half_2 = candles_half_1 * 2  

    # Calculate how many additional candles Stephanie needs to complete the cupcakes
    additional_candles = candles_half_1 + candles_half_2 - total_candles  

    result = additional_candles
    return result

print(solution())