def solution():
    hours_per_night = 2
    nights = 24

    # Calculate the number of hours the candle will burn over 24 nights
    total_hours = hours_per_night * nights

    # Calculate the number of candles Carmen will use over 24 nights
    num_candles = total_hours / 8
    result = num_candles
    return result

print(solution())