def solution():
    """Jeff’s swimming coach required him to swim 98 laps over the weekend. On Saturday, Jeff swam 27 laps. On Sunday morning, he swam 15 laps, took a break, then resumed practice in the afternoon. How many laps did Jeff have remaining when he took the break?"""
    total_laps = 98
    saturday_laps = 27
    sunday_morning_laps = 15
    remaining_laps = total_laps - saturday_laps - sunday_morning_laps
    result = remaining_laps
    return result

print(solution())