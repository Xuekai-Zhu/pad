def solution():
    total_beries = 30 + 20 + 10  # Iris, sister, and brother picked 30, 20, and 10 berries, respectively
    rotten_beries = total_beries / 3  # 1/3 of total berries are rotten
    fresh_beries = total_beries - rotten_beries  # Subtract rotten berries from total to get fresh berries
    berries_to_keep = fresh_beries / 2  # Half of the fresh berries need to be kept
    berries_to_sell = fresh_beries - berries_to_keep  # Subtract the berries to keep from fresh berries to get berries to sell
    result = berries_to_sell
    return result

print(solution())