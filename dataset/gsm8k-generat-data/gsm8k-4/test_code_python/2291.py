def solution():
    """Trish likes to go for walks every day. One day, she goes on a 1-mile walk. Every subsequent day, she doubles the distance she walked the previous day. On what day does she walk more than 10 times further than she did on the first day?"""
    
    # Define the initial distance and the target distance
    initial_distance = 1
    target_distance = 10 * initial_distance

    # Initialize the day counter and the current distance
    day = 1
    current_distance = initial_distance

    # Double the distance each day until it exceeds the target distance
    while current_distance < target_distance:
        day += 1
        current_distance *= 2

    # Return the day on which Trish walks more than 10 times further than the first day
    result = day
    return result

print(solution())