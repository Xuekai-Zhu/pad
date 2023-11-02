def solution():
    """It takes 3 beehives to make enough wax to make 12 candles. How many hives does it take to make 96 candles?"""
    candles_per_hive = 12 / 3
    hives_needed = 96 / candles_per_hive
    result = hives_needed
    return result

print(solution())