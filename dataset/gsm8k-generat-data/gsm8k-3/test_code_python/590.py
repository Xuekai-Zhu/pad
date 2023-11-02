def solution():
    """Makenna is selling candy for her Softball Team. The box contains 25 milk chocolate bars, 25 dark chocolate bars, 25 milk chocolate with almond bars, and 25 white chocolate bars. What is the percentage of each type of chocolate bar?"""
    # Define the total number of bars
    total_bars = 100

    # Calculate the percentage of milk chocolate bars
    milk_chocolate_percent = (25/total_bars) * 100

    # Calculate the percentage of dark chocolate bars
    dark_chocolate_percent = (25/total_bars) * 100

    # Calculate the percentage of milk chocolate with almond bars
    almond_chocolate_percent = (25/total_bars) * 100

    # Calculate the percentage of white chocolate bars
    white_chocolate_percent = (25/total_bars) * 100

    # Display the percentage of each type of chocolate bar
    result = [milk_chocolate_percent, dark_chocolate_percent, almond_chocolate_percent, white_chocolate_percent]
    return result

print(solution())