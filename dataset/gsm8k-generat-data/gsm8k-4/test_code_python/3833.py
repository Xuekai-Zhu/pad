def solution():
    """Alyssa and Chelsea jointly bought 40 candles to decorate their room. Alyssa used half of them, and Chelsea used 70% of the remaining candles. How many candles are there in the room now?"""
    # Define the initial number of candles
    initial_candles = 40

    # Calculate the number of candles used by Alyssa
    alyssa_candles = initial_candles / 2

    # Calculate the number of remaining candles
    remaining_candles = initial_candles - alyssa_candles

    # Calculate the number of candles used by Chelsea
    chelsea_candles = 0.7 * remaining_candles

    # Calculate the number of candles remaining in the room
    remaining_candles = remaining_candles - chelsea_candles

    # Return the result
    result = remaining_candles
    return result

print(solution())