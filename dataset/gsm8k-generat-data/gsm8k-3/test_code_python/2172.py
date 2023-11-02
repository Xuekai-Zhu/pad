def solution():
    """Kalani has twenty candles in her bedroom, twice the number of candles in the living room. Donovan, her brother, brings in 20 more candles he bought from the candle shop. What's the total number of candles in the house?"""
    # Calculate the number of candles in the living room
    living_room_candles = 20 / 2

    # Calculate the total number of candles before Donovan arrives
    total_candles = 20 + living_room_candles

    # Add Donovan's candles to the total
    total_candles += 20

    # Display the total number of candles
    result = total_candles
    return result

print(solution())