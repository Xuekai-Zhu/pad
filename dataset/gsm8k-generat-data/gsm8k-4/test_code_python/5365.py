def solution():
    """It takes 3 beehives to make enough wax to make 12 candles. How many hives does it take to make 96 candles?"""
    # Calculate the number of hives required to make 12 candles
    hives_for_12 = 3

    # Calculate the proportion of hives required to make 1 candle
    hives_for_1 = hives_for_12 / 12

    # Calculate the number of hives required to make 96 candles
    hives_for_96 = hives_for_1 * 96

    result = hives_for_96
    return result

print(solution())