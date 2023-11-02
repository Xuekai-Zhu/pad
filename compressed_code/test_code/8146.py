def solution():
    
    fences_built = 10
    time_per_fence = 30 
    total_time_available = 8 * 60 
    fences_buildable = total_time_available // time_per_fence
    total_fences_built = fences_built + fences_buildable
    result = total_fences_built
    return result

print(solution())