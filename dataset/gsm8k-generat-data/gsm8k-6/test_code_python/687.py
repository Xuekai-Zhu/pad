def solution():
    num_cupcakes = 24  # number of cupcakes Stephanie is decorating
    total_candles = 30  # total number of candles Stephanie currently has
    num_candles_per_set = 1 + 2  # total number of candles per set of cupcakes
    num_cupcakes_with_1_candle = num_cupcakes // 2  # number of cupcakes to decorate with 1 candle
    num_cupcakes_with_2_candles = num_cupcakes - num_cupcakes_with_1_candle  # number of cupcakes to decorate with 2 candles

    # Calculate the total number of candles needed to decorate the cupcakes
    total_candles_needed = (num_cupcakes_with_1_candle * 1) + (num_cupcakes_with_2_candles * 2)
    additional_candles_needed = total_candles_needed - total_candles  # Calculate how many additional candles Stephanie needs

    result = additional_candles_needed
    return result

print(solution())