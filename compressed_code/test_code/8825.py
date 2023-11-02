def solution():
    
    distance_to_school = 5000
    kernels_dropped_per_foot = 1/25
    total_kernels_dropped = kernels_dropped_per_foot * distance_to_school
    kernels_eaten_by_squirrel = total_kernels_dropped/4
    kernels_remaining = total_kernels_dropped - kernels_eaten_by_squirrel
    result = kernels_remaining
    return result

print(solution())