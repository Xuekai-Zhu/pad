def solution():
    """Diana needs to bike 10 miles to get home. She can bike 3 mph for two hours before she gets tired, and she can bike 1 mph until she gets home. How long will it take Diana to get home?"""
    # Define the total distance Diana needs to bike
    total_distance = 10

    # Define the speed at which Diana can bike for the first two hours and the time she can bike at that speed
    initial_speed = 3
    initial_time = 2

    # Define the speed at which Diana can bike for the remaining distance and the time it will take
    remaining_speed = 1
    remaining_distance = total_distance - (initial_speed * initial_time)
    remaining_time = remaining_distance / remaining_speed

    # Calculate the total time it will take for Diana to get home
    total_time = initial_time + remaining_time

    # Return the result
    result = total_time
    return result

print(solution())