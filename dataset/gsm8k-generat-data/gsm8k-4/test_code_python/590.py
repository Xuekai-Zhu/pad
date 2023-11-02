def solution():
    """Makenna is selling candy for her Softball Team. The box contains 25 milk chocolate bars, 25 dark chocolate bars, 25 milk chocolate with almond bars, and 25 white chocolate bars. What is the percentage of each type of chocolate bar?"""
    # Define the total number of chocolate bars
    total_bars = 100

    # Calculate the number of each type of chocolate bar
    milk_choc_bars = 25
    dark_choc_bars = 25
    almond_choc_bars = 25
    white_choc_bars = 25

    # Calculate the percentage of each type of chocolate bar
    milk_choc_percentage = (milk_choc_bars / total_bars) * 100
    dark_choc_percentage = (dark_choc_bars / total_bars) * 100
    almond_choc_percentage = (almond_choc_bars / total_bars) * 100
    white_choc_percentage = (white_choc_bars / total_bars) * 100

    # return the result
    result = [milk_choc_percentage, dark_choc_percentage, almond_choc_percentage, white_choc_percentage]
    return result

print(solution())