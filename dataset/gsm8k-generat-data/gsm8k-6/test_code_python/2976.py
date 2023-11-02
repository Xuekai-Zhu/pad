def solution():
    # Calculate the number of fences Abigail can build in 8 hours
    time_in_minutes = 8 * 60  # convert 8 hours to minutes
    num_fences_built = (time_in_minutes / 30) * 10  # each fence takes 30 minutes to build and she built 10 fences already
    result = num_fences_built
    return result

print(solution())