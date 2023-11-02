def solution():
    extra_feet_per_hour = 5
    hours_past_noon = 6
    inches_per_foot = 12

    # Calculate the total length of the shadows in feet
    total_feet = hours_past_noon * extra_feet_per_hour

    # Convert the total length of the shadows from feet to inches
    total_inches = total_feet * inches_per_foot
    result = total_inches
    return result

print(solution())