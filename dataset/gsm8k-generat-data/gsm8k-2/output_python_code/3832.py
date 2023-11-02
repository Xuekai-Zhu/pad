def solution():
    """Alyssa and Chelsea jointly bought 40 candles to decorate their room. Alyssa used half of them, and Chelsea used 70% of the remaining candles. How many candles are there in the room now?"""
    total_candles = 40
    alyssa_candles = total_candles // 2
    remaining_candles = total_candles - alyssa_candles
    chelsea_candles = int(0.7 * remaining_candles)
    total_candles_left = remaining_candles - chelsea_candles
    result = total_candles_left
    return result

print(solution())