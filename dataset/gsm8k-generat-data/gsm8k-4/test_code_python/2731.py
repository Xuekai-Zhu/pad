def solution():
    """Jeff’s swimming coach required him to swim 98 laps over the weekend. On Saturday, Jeff swam 27 laps. On Sunday morning, he swam 15 laps, took a break, then resumed practice in the afternoon. How many laps did Jeff have remaining when he took the break?"""
    # Define the total number of laps required and the number of laps Jeff swam on Saturday and Sunday morning
    total_laps = 98
    saturday_laps = 27
    sunday_morning_laps = 15

    # Calculate the remaining number of laps after Saturday and Sunday morning practice
    remaining_laps = total_laps - saturday_laps - sunday_morning_laps
    
    # Return the result
    result = remaining_laps
    return result

print(solution())