def solution():
    """Kalani has twenty candles in her bedroom, twice the number of candles in the living room. Donovan, her brother, brings in 20 more candles he bought from the candle shop. What's the total number of candles in the house?"""
    bedroom_candles = 20
    livingroom_candles = bedroom_candles / 2
    shop_candles = 20
    total_candles = bedroom_candles + livingroom_candles + shop_candles
    result = total_candles
    return result

print(solution())