def solution():
    
    journey_distance = 35
    portion_distance = journey_distance / 5
    speed = 40
    time = 0.7
    distance_traveled = speed * time
    portions_covered = distance_traveled / portion_distance
    result = portions_covered
    return result

print(solution())