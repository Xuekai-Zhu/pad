def solution():
    """It takes 3 beehives to make enough wax to make 12 candles. How many hives does it take to make 96 candles?"""
    hives_per_candle = 3/12
    candles_needed = 96
    hives_needed = candles_needed * hives_per_candle
    result = hives_needed
    return result

print(solution())