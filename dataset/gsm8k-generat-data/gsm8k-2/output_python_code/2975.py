def solution():
    """Abigail built 10 fences. Each fence took her 30 minutes to build. If she builds fences for the next 8 hours, how many fences would she have built in total?"""
    num_fences = 10
    time_per_fence = 30
    total_time = 8 * 60  # convert hours to minutes
    num_fences_built = num_fences + (total_time // time_per_fence)
    result = num_fences_built
    return result

print(solution())