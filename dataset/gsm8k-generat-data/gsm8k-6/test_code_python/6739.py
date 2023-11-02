def solution():
    # Calculate the total weight of beeswax used in making the candles
    beeswax_weight = 8 * (10-3)  # Ethan makes three less than 10 candles, so he makes 7 candles
    
    # Calculate the total weight of coconut oil used in making the candles
    coconut_oil_weight = 1 * (10-3)  # Ethan makes three less than 10 candles, so he makes 7 candles
    
    # Calculate the total weight of the candles
    total_candle_weight = beeswax_weight + coconut_oil_weight
    
    result = total_candle_weight
    return result

print(solution())