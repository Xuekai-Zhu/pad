def solution():
    """Carmen burns a candle for 1 hour every night. A candle will last her 8 nights. If she burns the candle for 2 hours a night, how many candles will she use over 24 nights?"""
    hours_per_candle = 8
    hours_per_night = 1
    candles_per_night_1_hour = 1 / hours_per_candle
    candles_per_night_2_hours = 2 / hours_per_candle
    total_nights = 24
    total_candles = (candles_per_night_1_hour * (total_nights // 2)) + (candles_per_night_2_hours * (total_nights // 2))
    if total_nights % 2 != 0:
        total_candles += candles_per_night_1_hour
    result = total_candles
    return result

print(solution())