def solution():
    
    distance_at_50mph = 50 * 3
    distance_at_80mph = 80 * 4
    total_distance = distance_at_50mph + distance_at_80mph
    distance_left = 600 - total_distance
    result = distance_left
    return result

print(solution())