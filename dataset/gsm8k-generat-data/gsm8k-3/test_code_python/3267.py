def solution():
    """Caleb is baking a birthday cake for his grandfather.
    His grandfather is turning 79 years old.
    Caleb puts three colors of candles on the cake.
    He puts one candle for each year for his grandfather.
    He puts 27 yellow candles, 14 red candles and the rest are blue candles.
    How many blue candles did he use?"""
    
    # Get the total number of candles used, which is the age of the grandfather
    total_candles = 79
    
    # Calculate the number of yellow and red candles used
    yellow_candles = 27
    red_candles = 14
    
    # Calculate the number of blue candles used by subtracting the yellow and red candles from the total
    blue_candles = total_candles - yellow_candles - red_candles
    
    # Display the number of blue candles used
    result = blue_candles
    return result

print(solution())