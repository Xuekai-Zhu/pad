def solution():
    """Kalani has twenty candles in her bedroom, twice the number of candles in the living room. Donovan, her brother, brings in 20 more candles he bought from the candle shop. What's the total number of candles in the house?"""
    # Define the number of candles in Kalani's bedroom and living room
    bedroom_candles = 20
    living_room_candles = bedroom_candles / 2

    # Add the number of candles brought in by Donovan
    total_candles = bedroom_candles + living_room_candles + 20

    # Return the result
    result = total_candles
    return result

print(solution())