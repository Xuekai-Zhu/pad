def solution():
    num_workers = 3
    num_chairs_per_hour = 4
    time_period = 6  # in hours

    # Calculate the total number of chairs produced by all workers during the time period
    total_chairs = num_workers * num_chairs_per_hour * time_period

    # Calculate the additional chair produced by the group during the time period
    additional_chairs = time_period // 6

    # Calculate the total number of chairs including the additional one
    total_chairs += additional_chairs

    result = total_chairs
    return result

print(solution())