def solution():
    """Bennett sells window screens. He sold twice as many window screens in February as he sold last month. In February, Bennett sold a fourth of what he sold in March. If Bennet sold 8800 window screens in March, how many screens did Bennett sell from January to March?"""
    # Calculate the number of screens sold in February
    screens_feb = 2 * screens_jan

    # Calculate the number of screens sold in March
    screens_mar = 8800

    # Calculate the number of screens sold in January
    screens_jan = screens_mar / (2/4 + 1)

    # Calculate the total number of screens sold from January to March
    total_screens = screens_jan + screens_feb + screens_mar

    # Display the total number of screens sold
    result = total_screens
    return result

print(solution())