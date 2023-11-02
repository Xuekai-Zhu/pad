def solution():
    # Define the amount of almond scent used per candle
    almond_scent = 1

    # Define the amount of coconut scent used per candle
    coconut_scent = 1.5 * almond_scent

    # Define the ratio of lavender candles to coconut candles
    lavender_to_coconut_ratio = 2

    # Calculate the total amount of almond scent used
    almond_scent_total = 10 * almond_scent

    # Calculate the total amount of coconut scent used
    coconut_scent_total = coconut_scent * almond_scent_total / almond_scent

    # Calculate the total amount of lavender scent used
    lavender_scent_total = (almond_scent_total + coconut_scent_total) / (lavender_to_coconut_ratio + 1)

    # Calculate the number of lavender candles made
    lavender_candles = lavender_scent_total / almond_scent

    result = lavender_candles
    return result

print(solution())