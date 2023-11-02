def solution():
    """Three train stations are 2 hours apart from one another. Kira travels from the first station to the third, taking a 30 minutes break at the second station. What's the total time, in minutes, that Kira takes to travel between the first and third station?"""
    # Define the distance between the stations in hours and the break time in minutes
    distance = 2
    break_time = 30

    # Calculate the total travel time in minutes, assuming an average speed of 60 mph
    total_time = (distance * 60) + break_time

    result = total_time
    return result

print(solution())