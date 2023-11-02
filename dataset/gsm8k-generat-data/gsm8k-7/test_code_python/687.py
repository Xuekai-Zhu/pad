def solution():
    num_cupcakes = 24
    total_candles = 30

    # Calculate the number of cupcakes that will have 1 candle
    num_cupcakes_1_candle = num_cupcakes // 2

    # Calculate the number of cupcakes that will have 2 candles
    num_cupcakes_2_candles = num_cupcakes - num_cupcakes_1_candle

    # Calculate the total number of candles needed for cupcakes with 1 candle
    total_candles_1_candle = num_cupcakes_1_candle

    # Calculate the total number of candles needed for cupcakes with 2 candles
    total_candles_2_candles = num_cupcakes_2_candles * 2

    # Calculate the total number of candles needed for all cupcakes
    total_candles_needed = total_candles_1_candle + total_candles_2_candles

    # Calculate the number of additional candles needed
    additional_candles_needed = total_candles_needed - total_candles

    result = additional_candles_needed
    return result

print(solution())