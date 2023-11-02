def solution():
    """Alyssa and Chelsea jointly bought 40 candles to decorate their room. Alyssa used half of them, and Chelsea used 70% of the remaining candles. How many candles are there in the room now?"""
    candles = 40
    alyssa_used = candles / 2
    remaining_candles = candles - alyssa_used
    chelsea_used = remaining_candles * 0.7
    total_used = alyssa_used + chelsea_used
    remaining_candles = candles - total_used
    result = remaining_candles
    return result

print(solution())