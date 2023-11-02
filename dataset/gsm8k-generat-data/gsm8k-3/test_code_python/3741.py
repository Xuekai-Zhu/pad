def solution():
    """Roger uses his lunch break to walk the stairs in his office building.  He can walk 2,000 steps in 30 minutes.  If his daily goal is 10,000 steps, how many minutes will it take him to reach his goal?"""
    # Calculate the number of minutes it takes Roger to walk 1,000 steps
    minutes_per_1000_steps = 30 / 2000 * 1000

    # Calculate the total number of minutes it will take Roger to reach his goal
    total_minutes = minutes_per_1000_steps * 10

    # Display the total minutes
    result = total_minutes
    return result

print(solution())