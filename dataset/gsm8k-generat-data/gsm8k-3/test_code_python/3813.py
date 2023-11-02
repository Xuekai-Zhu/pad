def solution():
    """Carmen burns a candle for 1 hour every night. A candle will last her 8 nights. 
    If she burns the candle for 2 hours a night, how many candles will she use over 24 nights?"""
    
    # Calculate the number of candles used if burned for 1 hour per night
    candles_1hr = 24 // 8
    
    # Calculate the number of candles used if burned for 2 hours per night
    candles_2hr = (24 * 2) // 8
    
    # Display the total number of candles used
    result = candles_2hr
    return result

print(solution())