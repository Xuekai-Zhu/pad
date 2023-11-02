def solution():
    """Jill makes scented candles as a hobby. Her favorite scents are lavender, coconut, and almond, and she uses the same amount of each scent for every candle. This time, she made twice as many lavender candles as coconut candles, along with a batch of almond candles. She ran out of almond scent after making ten candles. If she had one and a half times as much coconut scent as almond scent and used all her coconut scent up too, how many lavender candles did she make?"""
    # Define the number of almond candles made
    almond_candles = 10

    # Calculate the amount of coconut scent Jill had
    coconut_scent = 1.5 * almond_candles

    # Calculate the total number of candles made
    total_candles = almond_candles + (coconut_scent / 3) + (2 * (coconut_scent / 3))

    # Calculate the number of lavender candles made
    lavender_candles = total_candles / 3

    # Display the number of lavender candles made
    result = lavender_candles
    return result

print(solution())