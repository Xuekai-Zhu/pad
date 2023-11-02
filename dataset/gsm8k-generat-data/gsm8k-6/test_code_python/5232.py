def solution():
    almond_candles = 10  # Jill ran out of almond scent after making 10 candles
    coconut_scent = 1.5 * almond_candles  # Jill had 1.5 times as much coconut scent as almond scent
    total_candles = almond_candles + (coconut_scent/3) + (2*coconut_scent/3)  # Jill made twice as many lavender candles as coconut candles
    lavender_candles = 2*(coconut_scent/3)  # Jill made twice as many lavender candles as coconut candles
    result = lavender_candles
    return result

print(solution())