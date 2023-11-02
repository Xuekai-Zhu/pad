def solution():
    """Every ten minutes during sunset, the sky changes to a new color. How many colors did the sky turn over the two hours of a long summer sunset if each hour is sixty minutes long?"""
    colors_per_hour = 6  # 60 minutes divided by 10 minute intervals
    hours = 2
    total_colors = colors_per_hour * hours
    result = total_colors
    return result

print(solution())