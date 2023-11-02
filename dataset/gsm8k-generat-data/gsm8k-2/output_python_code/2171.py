def solution():
    """Kalani has twenty candles in her bedroom, twice the number of candles in the living room. Donovan, her brother, brings in 20 more candles he bought from the candle shop. What's the total number of candles in the house?"""
    kalani_bedroom_candles = 20
    living_room_candles = kalani_bedroom_candles / 2
    donovan_candles = 20
    total_candles = kalani_bedroom_candles + living_room_candles + donovan_candles
    result = total_candles
    return result

print(solution())