def solution():
    # Calculate the time it takes for John to finish the race
    time_John = 5 / 15 * 60  # convert miles per hour to minutes per mile

    # Calculate the time it takes for the next fastest guy to finish the race
    time_next_fastest = 23

    # Calculate the time difference between John and the next fastest guy
    time_difference = time_next_fastest - time_John

    result = time_difference
    return result

print(solution())