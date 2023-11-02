def solution():
    # Calculate how long one candle lasts in hours
    candle_duration = 8 * 1  # 8 nights, with 1 hour of burning each night

    # Calculate how many candles Carmen will use over 24 nights if she burns the candle for 2 hours each night
    total_candles = 24 // 8  # How many sets of 8 nights there will be
    if 24 % 8 != 0:  # If there's an incomplete set of 8 nights
        remaining_nights = 24 % 8
        if remaining_nights <= 2:  # If there are 2 or fewer remaining nights, only 1 candle will be used
            total_candles += 1
        else:
            total_candles += 2  # Otherwise, 2 candles will be used

    result = total_candles
    return result

print(solution())