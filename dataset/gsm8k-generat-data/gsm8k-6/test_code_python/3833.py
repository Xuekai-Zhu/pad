def solution():
    total_candles = 40  # total number of candles
    alyssa_candles = total_candles / 2  # Alyssa uses half of the candles
    remaining_candles = total_candles - alyssa_candles  # number of candles remaining
    chelsea_candles = 0.7 * remaining_candles  # Chelsea uses 70% of the remaining candles
    candles_in_room = remaining_candles - chelsea_candles  # number of candles in the room now
    result = candles_in_room
    return result

print(solution())