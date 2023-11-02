def solution():
    """Joan wants to visit her family who live 480 miles away. If she drives at a rate of 60 mph and takes a lunch break taking 30 minutes, and 2 bathroom breaks taking 15 minutes each, how many hours did it take her to get there?"""
    
    # Define the distance in miles and the speed in miles per hour
    distance = 480
    speed = 60

    # Calculate the time it takes to travel without any breaks
    time_without_breaks = distance / speed

    # Calculate the total time spent on breaks
    total_break_time = (30 + 2 * 15) / 60

    # Calculate the total time it takes to travel with breaks
    total_time = time_without_breaks + total_break_time

    # Return the result in hours
    result = total_time
    return result

print(solution())