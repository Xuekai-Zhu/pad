def solution():
    
    num_fences = 10
    time_per_fence = 30
    total_time = 8 * 60  
    num_fences_built = num_fences + (total_time // time_per_fence)
    result = num_fences_built
    return result

print(solution())