def solution():
    """Carmen burns a candle for 1 hour every night. A candle will last her 8 nights. If she burns the candle for 2 hours a night, how many candles will she use over 24 nights?"""
    # Define the number of nights Carmen burns the candle and the number of hours each night
    nights = 24
    hours_per_night = 2

    # Calculate the number of candles Carmen will use over 24 nights
    total_hours = nights * hours_per_night
    candles_used = total_hours / 8

    # Round up to the nearest whole number of candles
    candles_used = int(candles_used + 0.5)

    # return the result
    result = candles_used
    return result

print(solution())