def solution():
    lavender_ratio = 2
    coconut_ratio = 1
    almond_ratio = 1
    almond_batch = 10

    coconut_ratio = 1.5 * almond_ratio
    total_ratio = lavender_ratio + coconut_ratio + almond_ratio

    # Calculate the total number of candles made
    total_candles = almond_batch / almond_ratio * total_ratio

    # Calculate the number of lavender candles made
    lavender_candles = total_candles / total_ratio * lavender_ratio
    result = lavender_candles
    return result

print(solution())