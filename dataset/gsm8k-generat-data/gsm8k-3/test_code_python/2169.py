def solution():
    """John manages to run 15 mph for his whole 5-mile race.  The next fastest guy ran the race in 23 minutes.  How many minutes did he win the race by?"""
    
    # Convert John's speed to miles per minute
    john_speed = 15 / 60

    # Calculate the time it took John to complete the race
    john_time = 5 / john_speed

    # Calculate the time it took the next fastest guy to complete the race
    next_fastest_time = 23

    # Calculate the difference in time between John and the next fastest guy
    time_difference = john_time - (next_fastest_time / 60)

    # Convert the time difference to minutes and round to the nearest minute
    time_difference_minutes = round(time_difference * 60)

    # Display the number of minutes John won the race by
    result = time_difference_minutes
    return result

print(solution())