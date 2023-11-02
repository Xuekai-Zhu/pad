def solution():
    """Makenna is selling candy for her Softball Team. The box contains 25 milk chocolate bars, 25 dark chocolate bars, 25 milk chocolate with almond bars, and 25 white chocolate bars. What is the percentage of each type of chocolate bar?"""
    total_bars = 100
    milk_chocolate_bars = 25
    dark_chocolate_bars = 25
    milk_almond_bars = 25
    white_chocolate_bars = 25
    
    milk_chocolate_percent = (milk_chocolate_bars / total_bars) * 100
    dark_chocolate_percent = (dark_chocolate_bars / total_bars) * 100
    milk_almond_percent = (milk_almond_bars / total_bars) * 100
    white_chocolate_percent = (white_chocolate_bars / total_bars) * 100
    
    result = (milk_chocolate_percent, dark_chocolate_percent, milk_almond_percent, white_chocolate_percent)
    return result

print(solution())