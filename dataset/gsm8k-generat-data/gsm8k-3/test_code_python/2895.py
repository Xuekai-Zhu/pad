def solution():
    """Joan wants to visit her family who live 480 miles away.  If she drives at a rate of 60 mph and takes a lunch break taking 30 minutes, and 2 bathroom breaks taking 15 minutes each, how many hours did it take her to get there?"""
    # Define the total distance to Joan's family
    distance = 480

    # Define Joan's driving speed
    speed = 60

    # Define the time for each break
    lunch_break = 0.5
    bathroom_breaks = 0.5

    # Calculate the total time for breaks
    total_break_time = lunch_break + (2 * bathroom_breaks)

    # Calculate the total driving time
    driving_time = distance / speed

    # Calculate the total travel time including breaks
    total_travel_time = driving_time + total_break_time

    # Display the total travel time
    result = total_travel_time
    return result

print(solution())