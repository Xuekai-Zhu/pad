def solution():
    
    total_crickets = 70
    first_day_crickets = total_crickets * 0.3
    second_day_crickets = first_day_crickets - 6
    third_day_crickets = total_crickets - first_day_crickets - second_day_crickets
    result = third_day_crickets
    return result

print(solution())