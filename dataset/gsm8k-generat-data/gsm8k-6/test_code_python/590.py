def solution():
    # Calculate the percentage of each type of chocolate bar
    total_bars = 25*4  # total number of chocolate bars in the box
    milk_choc_percent = (25/total_bars) * 100  # percentage of milk chocolate bars
    dark_choc_percent = (25/total_bars) * 100  # percentage of dark chocolate bars
    milk_almond_percent = (25/total_bars) * 100  # percentage of milk chocolate with almond bars
    white_choc_percent = (25/total_bars) * 100  # percentage of white chocolate bars
    result = (milk_choc_percent, dark_choc_percent, milk_almond_percent, white_choc_percent)
    return result

print(solution())