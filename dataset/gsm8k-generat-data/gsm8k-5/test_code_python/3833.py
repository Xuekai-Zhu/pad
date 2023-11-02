def solution():
    total_candles = 40  # Alyssa and Chelsea had 40 candles to begin with

    # Alyssa used half of the candles
    alyssa_candles = total_candles // 2

    # Chelsea used 70% of the remaining candles
    remaining_candles = total_candles - alyssa_candles
    chelsea_candles = remaining_candles * 0.7

    # Calculate the total number of candles left in the room
    total_left = alyssa_candles + chelsea_candles
    result = total_left
    return result

print(solution())