def solution():
    # Calculate the total number of chocolate bars
    total_bars = 25 * 4

    # Calculate the number of each type of chocolate bar
    milk_choc_bars = 25
    dark_choc_bars = 25
    almond_choc_bars = 25
    white_choc_bars = 25

    # Calculate the percentage of each type of chocolate bar
    milk_choc_percent = (milk_choc_bars / total_bars) * 100
    dark_choc_percent = (dark_choc_bars / total_bars) * 100
    almond_choc_percent = (almond_choc_bars / total_bars) * 100
    white_choc_percent = (white_choc_bars / total_bars) * 100

    result = (milk_choc_percent, dark_choc_percent, almond_choc_percent, white_choc_percent)
    return result

print(solution())