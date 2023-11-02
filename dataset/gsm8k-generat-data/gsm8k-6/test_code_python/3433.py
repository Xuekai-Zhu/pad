def solution():
    # Calculate how far the first runner is ahead of the second runner after 56 minutes
    distance_first_runner = 56 / 8  # first runner's distance in miles
    distance_second_runner = 56 / 7  # second runner's distance in miles
    distance_difference = distance_first_runner - distance_second_runner

    # Calculate how long it will take the first runner to catch up with the second runner
    time_to_catch_up = distance_difference / (8/60 - 7/60)  # difference in pace is 1 minute per mile, converted to hours
    time_stopped = time_to_catch_up - (56 / 60)  # subtract the initial 56 minutes of running
    result = time_stopped * 60  # convert back to minutes
    return result

print(solution())