def solution():
    total_bars = 25 * 4

    # Calculate the percentage of milk chocolate bars
    milk_bars = 25
    milk_percent = (milk_bars / total_bars) * 100

    # Calculate the percentage of dark chocolate bars
    dark_bars = 25
    dark_percent = (dark_bars / total_bars) * 100

    # Calculate the percentage of milk chocolate with almond bars
    almond_bars = 25
    almond_percent = (almond_bars / total_bars) * 100

    # Calculate the percentage of white chocolate bars
    white_bars = 25
    white_percent = (white_bars / total_bars) * 100

    result = (milk_percent, dark_percent, almond_percent, white_percent)
    return result

print(solution())