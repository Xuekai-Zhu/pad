def solution():
    """John manages to run 15 mph for his whole 5-mile race. The next fastest guy ran the race in 23 minutes. How many minutes did he win the race by?"""
    # Calculate John's time to complete the race in minutes
    john_time = (5 / 15) * 60

    # Calculate the time of the next fastest guy in minutes
    next_fastest = 23

    # Calculate the time difference between John and the next fastest guy in minutes
    time_difference = john_time - next_fastest

    # Display the time John won the race by
    result = time_difference
    return result

print(solution())