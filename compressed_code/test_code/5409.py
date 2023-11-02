def solution():
    
    hours_per_week = 30
    hours_per_painting = 3
    paintings_per_week = hours_per_week // hours_per_painting
    total_paintings = paintings_per_week * 4
    result = total_paintings
    return result

print(solution())