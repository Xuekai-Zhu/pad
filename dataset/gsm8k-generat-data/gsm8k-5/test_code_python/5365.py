def solution():
    # Find how many candles can be made from 1 hive
    candles_per_hive = 12/3

    # Find how many hives are needed to make 96 candles
    hives_needed = 96/candles_per_hive

    result = hives_needed
    return result

print(solution())