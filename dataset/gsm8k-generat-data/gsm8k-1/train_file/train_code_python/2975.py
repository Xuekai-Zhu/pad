def solution():
    """Abigail built 10 fences. Each fence took her 30 minutes to build. If she builds fences for the next 8 hours, how many fences would she have built in total?"""
    fences_built = 10
    time_per_fence = 30 # in minutes
    total_time_available = 8 * 60 # in minutes
    fences_buildable = total_time_available // time_per_fence
    total_fences_built = fences_built + fences_buildable
    result = total_fences_built
    return result

print(solution())