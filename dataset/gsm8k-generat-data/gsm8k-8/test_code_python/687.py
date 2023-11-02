def solution():
    total_cupcakes = 24
    total_candles = 30

    # Calculate the number of cupcakes with 1 candle
    cupcakes_with_1_candle = total_cupcakes // 2

    # Calculate the number of cupcakes with 2 candles
    cupcakes_with_2_candles = total_cupcakes - cupcakes_with_1_candle

    # Calculate the total number of candles needed
    total_candles_needed = cupcakes_with_1_candle + (2 * cupcakes_with_2_candles)

    # Calculate the additional candles needed
    additional_candles_needed = total_candles_needed - total_candles
    result = additional_candles_needed
    return result

print(solution())