def solution():
    # Define the variables and constants
    distance = 480
    speed = 60
    lunch_break = 0.5
    bathroom_breaks = 2 * 0.25

    # Calculate the time it takes to drive to the destination
    travel_time = distance / speed

    # Add the time for the breaks
    total_time = travel_time + lunch_break + bathroom_breaks

    # Round the result to two decimal places
    result = round(total_time, 2)
    return result

print(solution())