def solution():
    work_minutes = 240  # James works for 240 minutes
    water_break_interval = 20  # James takes a water break every 20 minutes
    sitting_break_interval = 120  # James takes a sitting break every 120 minutes

    # Calculate the number of water breaks and sitting breaks James takes
    water_breaks = work_minutes // water_break_interval
    sitting_breaks = work_minutes // sitting_break_interval

    # Calculate the difference in the number of water breaks and sitting breaks
    diff = water_breaks - sitting_breaks
    result = diff
    return result

print(solution())