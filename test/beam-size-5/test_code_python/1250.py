def solution():
    
    old_time_per_painting = 7
    new_time_per_painting = 12
    old_paintings = 6
    new_paintings = 6
    old_total_time = old_paintings * old_time_per_painting
    new_total_time = new_paintings * new_time_per_painting
    extra_time = new_total_time - old_total_time
    result = extra_time
    return result

print(solution())