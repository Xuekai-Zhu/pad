def solution():
    """A train takes 4 hours to reach a destination at a speed of 50 miles per hour. How long would it take if it traveled at 100 miles per hour instead?"""
    # Define the initial variables
    initial_speed = 50
    initial_time = 4
    final_speed = 100

    # Use the formula distance = speed * time to calculate the initial distance
    initial_distance = initial_speed * initial_time

    # Use the same formula to calculate the final time, given the new speed and the initial distance
    final_time = initial_distance / final_speed

    # Display the final time
    result = final_time
    return result

print(solution())