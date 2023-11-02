def solution():
    num_fences = 10
    time_per_fence = 30  # in minutes
    total_time = 8 * 60  # in minutes

    # Calculate the total number of fences Abigail can build in the given time
    total_fences = (total_time / time_per_fence) + num_fences
    result = total_fences
    return result

print(solution())