def solution():
    """Jill makes scented candles as a hobby. Her favorite scents are lavender, coconut, and almond, and she uses the same amount of each scent for every candle. This time, she made twice as many lavender candles as coconut candles, along with a batch of almond candles. She ran out of almond scent after making ten candles. If she had one and a half times as much coconut scent as almond scent and used all her coconut scent up too, how many lavender candles did she make?"""

    # Define the ratio of scents used
    lavender_ratio = 1
    coconut_ratio = 0.5
    almond_ratio = 1

    # Set the number of almond candles made
    almond_candles = 10

    # Calculate the total amount of coconut scent used
    coconut_scent_total = almond_candles * almond_ratio * coconut_ratio + coconut_candles * coconut_ratio

    # Calculate the number of coconut candles made
    coconut_candles = coconut_scent_total / (coconut_ratio * lavender_ratio * 2)

    # Calculate the number of lavender candles made
    lavender_candles = coconut_candles * 2

    result = lavender_candles
    return result

print(solution())