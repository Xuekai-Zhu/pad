def solution():
    """A train takes 4 hours to reach a destination at a speed of 50 miles per hour. How long would it take if it traveled at 100 miles per hour instead?"""
    # Define the initial speed and time
    initial_speed = 50
    initial_time = 4

    # Calculate the initial distance
    initial_distance = initial_speed * initial_time

    # Calculate the new time for the increased speed
    new_speed = 100
    new_time = initial_distance / new_speed

    result = new_time
    return result

print(solution())