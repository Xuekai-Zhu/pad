def solution():
    # Calculate how long the candle lasts with a one hour burn time
    one_hour_burn = 8
    # Calculate how long the candle lasts with a two hour burn time
    two_hour_burn = one_hour_burn / 2
    # Calculate how many candles Carmen will use over 24 nights
    total_nights = 24
    num_candles_used = total_nights / two_hour_burn
    result = num_candles_used
    return result

print(solution())