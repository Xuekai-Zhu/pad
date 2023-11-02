def solution():
    total_minutes = 240
    water_break_freq = 20
    sitting_break_freq = 120

    # Calculate the total number of water breaks taken by James
    total_water_breaks = total_minutes // water_break_freq

    # Calculate the total number of sitting breaks taken by James
    total_sitting_breaks = total_minutes // sitting_break_freq

    # Calculate the difference between the number of water breaks and sitting breaks
    diff = total_water_breaks - total_sitting_breaks
    result = diff
    return result

print(solution())