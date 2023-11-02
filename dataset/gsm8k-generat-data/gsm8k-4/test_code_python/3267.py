def solution():
    """Caleb is baking a birthday cake for his grandfather. His grandfather is turning 79 years old. Caleb puts three colors of candles on the cake. He puts one candle for each year for his grandfather. He puts 27 yellow candles, 14 red candles and the rest are blue candles. How many blue candles did he use?"""
    # Define the age of Caleb's grandfather
    grandfather_age = 79

    # Calculate the total number of candles on the cake
    total_candles = grandfather_age

    # Calculate the number of yellow and red candles
    yellow_candles = 27
    red_candles = 14

    # Calculate the number of blue candles
    blue_candles = total_candles - yellow_candles - red_candles

    # return the result
    result = blue_candles
    return result

print(solution())