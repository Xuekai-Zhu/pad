def solution():
    num_candles_per_hive = 12 / 3 # 4 candles per hive
    num_candles = 96
    num_hives = num_candles / num_candles_per_hive
    result = num_hives
    return result

print(solution())