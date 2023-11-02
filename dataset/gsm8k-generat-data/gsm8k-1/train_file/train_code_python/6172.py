def solution():
    """Aniyah has 6 times as many birthday candles as Ambika. If Ambika has four birthday candles, how many birthday candles will they have if they put the birthday candles together and shared them equally between themselves?"""
    ambika_candles = 4
    aniyah_candles = ambika_candles * 6
    total_candles = ambika_candles + aniyah_candles
    candles_each = total_candles // 2
    result = candles_each
    return result

print(solution())