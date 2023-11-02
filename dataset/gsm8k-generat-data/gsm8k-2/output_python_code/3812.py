def solution():
    """Carmen burns a candle for 1 hour every night. A candle will last her 8 nights. If she burns the candle for 2 hours a night, how many candles will she use over 24 nights?"""
    candle_hours = 8
    one_hour_nights = candle_hours * 1
    two_hour_nights = 8 - 1
    total_candles = 24 / 8 * 1 + 24 / 8 * 2
    result = total_candles
    return result

print(solution())