def solution():
    """Aniyah has 6 times as many birthday candles as Ambika. If Ambika has four birthday candles, how many birthday candles will they have if they put the birthday candles together and shared them equally between themselves?"""
    ambika_candles = 4
    aniyah_candles = 6 * ambika_candles
    total_candles = ambika_candles + aniyah_candles
    equal_share = total_candles / 2
    result = equal_share
    return result

print(solution())