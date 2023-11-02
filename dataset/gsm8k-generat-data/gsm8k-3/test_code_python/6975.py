def solution():
    """To make 3 km, Ben walked for 2 hours. Continuing at the same speed, how much time in minutes would it take him to travel 12 km?"""
    # Calculate Ben's speed in km per hour
    speed = 3 / 2

    # Calculate how many hours Ben will take to travel 12 km
    time_in_hours = 12 / speed

    # Convert the time to minutes
    time_in_minutes = time_in_hours * 60

    # Display the time in minutes
    result = time_in_minutes
    return result

print(solution())