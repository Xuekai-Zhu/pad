def solution():
    """Jeff’s swimming coach required him to swim 98 laps over the weekend. On Saturday, Jeff swam 27 laps. On Sunday morning, he swam 15 laps, took a break, then resumed practice in the afternoon. How many laps did Jeff have remaining when he took the break?"""
    total_laps = 98
    laps_on_saturday = 27
    laps_on_sunday_morning = 15
    laps_remaining = total_laps - laps_on_saturday - laps_on_sunday_morning
    result = laps_remaining
    return result

print(solution())