def solution():
    
    total_distance = 35
    portions = 5
    distance_per_portion = total_distance / portions
    speed = 40
    time = 0.7
    distance_traveled = speed * time
    portions_covered = distance_traveled / distance_per_portion
    result = portions_covered
    return result

print(solution())