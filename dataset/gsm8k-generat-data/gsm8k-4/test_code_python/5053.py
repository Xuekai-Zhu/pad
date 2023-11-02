def solution():
    """Every ten minutes during sunset, the sky changes to a new color. How many colors did the sky turn over the two hours of a long summer sunset if each hour is sixty minutes long?"""
    # Define the number of colors in a ten-minute interval
    colors_per_interval = 1

    # Define the number of intervals in an hour
    intervals_per_hour = 6

    # Define the total number of hours
    total_hours = 2

    # Calculate the total number of colors
    total_colors = colors_per_interval * intervals_per_hour * total_hours

    # return the result
    result = total_colors
    return result

print(solution())