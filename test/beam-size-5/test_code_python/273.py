def solution():
    
    small_holes_time = 3
    large_holes_time = 10
    small_holes = 30
    large_holes = 15
    total_time = (small_holes * small_holes_time) + (large_holes * large_holes_time)
    hours = total_time / 60
    result = hours
    return result

print(solution())