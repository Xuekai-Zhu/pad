def solution():
    sunset_time = 120  # The sunset lasts for 2 hours, or 120 minutes
    color_change_interval = 10  # The sky changes to a new color every 10 minutes

    # Calculate the number of color changes during the sunset
    color_changes = sunset_time // color_change_interval

    result = color_changes
    return result

print(solution())