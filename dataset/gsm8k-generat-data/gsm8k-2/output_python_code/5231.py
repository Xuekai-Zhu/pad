def solution():
    """Jill makes scented candles as a hobby. Her favorite scents are lavender, coconut, and almond, and she uses the same amount of each scent for every candle. This time, she made twice as many lavender candles as coconut candles, along with a batch of almond candles. She ran out of almond scent after making ten candles. If she had one and a half times as much coconut scent as almond scent and used all her coconut scent up too, how many lavender candles did she make?"""
    almond_candles = 10
    coconut_scent = 1.5 * almond_candles
    total_candles = almond_candles + (coconut_scent / 3) + ((2 * coconut_scent) / 3)
    lavender_candles = 2 * (total_candles / 3)
    result = lavender_candles
    return result

print(solution())