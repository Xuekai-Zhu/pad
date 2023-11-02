def solution():
    """Every ten minutes during sunset, the sky changes to a new color. How many colors did the sky turn over the two hours of a long summer sunset if each hour is sixty minutes long?"""
    color_change_interval = 10
    sunset_duration = 120
    num_color_changes = sunset_duration // color_change_interval
    result = num_color_changes
    return result

print(solution())