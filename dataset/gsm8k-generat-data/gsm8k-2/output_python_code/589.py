def solution():
    """Makenna is selling candy for her Softball Team. The box contains 25 milk chocolate bars, 25 dark chocolate bars, 25 milk chocolate with almond bars, and 25 white chocolate bars. What is the percentage of each type of chocolate bar?"""
    total_bars = 100
    milk_chocolate_bars = 25
    dark_chocolate_bars = 25
    milk_almond_bars = 25
    white_chocolate_bars = 25
    milk_percentage = milk_chocolate_bars / total_bars * 100
    dark_percentage = dark_chocolate_bars / total_bars * 100
    almond_percentage = milk_almond_bars / total_bars * 100
    white_percentage = white_chocolate_bars / total_bars * 100
    result = (milk_percentage, dark_percentage, almond_percentage, white_percentage)
    return result

print(solution())