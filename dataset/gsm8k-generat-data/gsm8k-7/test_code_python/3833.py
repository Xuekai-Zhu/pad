def solution():
    total_candles = 40
    alyssa_used = total_candles / 2
    remaining_candles = total_candles - alyssa_used
    chelsea_used = 0.7 * remaining_candles
    remaining_candles -= chelsea_used
    result = remaining_candles
    return result

print(solution())