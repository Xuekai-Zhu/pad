def solution():
    """Alyssa and Chelsea jointly bought 40 candles to decorate their room. Alyssa used half of them, and Chelsea used 70% of the remaining candles. How many candles are there in the room now?"""
    # Define the number of candles bought
    TOTAL_CANDLES = 40

    # Calculate the number of candles used by Alyssa
    alyssa_candles = TOTAL_CANDLES // 2

    # Calculate the number of candles remaining
    remaining_candles = TOTAL_CANDLES - alyssa_candles

    # Calculate the number of candles used by Chelsea
    chelsea_candles = int(remaining_candles * 0.7)

    # Calculate the number of candles left in the room
    candles_left = remaining_candles - chelsea_candles

    # Display the number of candles left in the room
    result = candles_left
    return result

print(solution())