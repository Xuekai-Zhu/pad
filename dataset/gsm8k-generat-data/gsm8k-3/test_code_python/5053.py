def solution():
    """Every ten minutes during sunset, the sky changes to a new color. How many colors did the sky turn over the two hours of a long summer sunset if each hour is sixty minutes long?"""
    # Calculate the number of 10-minute intervals in 2 hours
    intervals = 2 * 60 / 10

    # Calculate the number of colors the sky turned
    colors = intervals + 1

    # Display the number of colors
    result = colors
    return result

print(solution())