def solution():
    """Jeff’s swimming coach required him to swim 98 laps over the weekend. On Saturday, Jeff swam 27 laps. On Sunday morning, he swam 15 laps, took a break, then resumed practice in the afternoon. How many laps did Jeff have remaining when he took the break?"""
    # Define the number of laps Jeff swam
    saturday_laps = 27
    sunday_morning_laps = 15
    total_laps = 98

    # Calculate the number of laps Jeff swam on Sunday afternoon
    sunday_afternoon_laps = total_laps - saturday_laps - sunday_morning_laps

    # Calculate the number of laps Jeff had remaining when he took the break
    remaining_laps = sunday_afternoon_laps

    # Display the number of laps Jeff had remaining
    result = remaining_laps
    return result

print(solution())