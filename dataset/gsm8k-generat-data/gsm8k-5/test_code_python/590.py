def solution():
    total_bars = 100  # The box contains 100 chocolate bars in total
    milk_chocolate_bars = 25  # There are 25 milk chocolate bars in the box
    dark_chocolate_bars = 25  # There are 25 dark chocolate bars in the box
    milk_almond_chocolate_bars = 25  # There are 25 milk chocolate with almond bars in the box
    white_chocolate_bars = 25  # There are 25 white chocolate bars in the box

    # Calculate the percentage of each type of chocolate bar
    milk_chocolate_percentage = (milk_chocolate_bars / total_bars) * 100
    dark_chocolate_percentage = (dark_chocolate_bars / total_bars) * 100
    milk_almond_chocolate_percentage = (milk_almond_chocolate_bars / total_bars) * 100
    white_chocolate_percentage = (white_chocolate_bars / total_bars) * 100

    result = (milk_chocolate_percentage, dark_chocolate_percentage, milk_almond_chocolate_percentage, white_chocolate_percentage)
    return result

print(solution())