def solution():
    
    walk_time = 1
    walk_distance = 4
    days_not_walked = 4
    days_walked = 31 - days_not_walked
    total_distance = days_walked * walk_time * walk_distance
    result = total_distance
    return result

print(solution())