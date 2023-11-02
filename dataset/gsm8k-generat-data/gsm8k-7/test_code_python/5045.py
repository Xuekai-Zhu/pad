def solution():
    last_week_ropes = 6
    this_week_ropes = last_week_ropes - 4
    feet_to_inches = 12

    # Convert both weeks' rope lengths from feet to inches
    last_week_inches = last_week_ropes * feet_to_inches
    this_week_inches = this_week_ropes * feet_to_inches

    # Calculate the total length of rope in inches that Mr. Sanchez bought
    total_inches = last_week_inches + this_week_inches
    result = total_inches
    return result

print(solution())