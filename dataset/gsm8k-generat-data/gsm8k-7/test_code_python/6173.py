def solution():
    ambika_candles = 4
    aniyah_candles = 6 * ambika_candles
    total_candles = ambika_candles + aniyah_candles

    # split the total number of candles equally
    equal_share = total_candles / 2
    result = equal_share
    return result

print(solution())