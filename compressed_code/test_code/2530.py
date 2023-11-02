def solution():
    
    small_bands = 50
    large_bands = 300
    total_bands = 5000
    small_balls = 22
    used_bands = small_balls * small_bands
    remaining_bands = total_bands - used_bands
    large_balls = remaining_bands // large_bands
    result = large_balls
    return result

print(solution())