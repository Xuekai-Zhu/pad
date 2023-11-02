def solution():
    """Caleb is baking a birthday cake for his grandfather. His grandfather is turning 79 years old. Caleb puts three colors of candles on the cake. He puts one candle for each year for his grandfather. He puts 27 yellow candles, 14 red candles and the rest are blue candles. How many blue candles did he use?"""
    grandfather_age = 79
    yellow_candles = 27
    red_candles = 14
    total_candles = grandfather_age
    blue_candles = total_candles - yellow_candles - red_candles
    result = blue_candles
    return result

print(solution())