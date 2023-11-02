def solution():
    # Calculate the total distance of the race
    distance = 7 * 3/4

    # Calculate the speed of this year's winner in miles per minute
    speed_this_year = distance / 42

    # Calculate the speed of last year's winner in miles per minute
    speed_last_year = distance / 47.25

    # Calculate the time difference for one mile of the race
    time_difference = (1/speed_last_year - 1/speed_this_year) * 60

    result = time_difference
    return result

print(solution())