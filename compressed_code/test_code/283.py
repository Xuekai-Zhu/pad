def solution():
    
    starting_distance = 2
    target_distance = 20
    distance_increase_per_week = 2/3
    total_distance_to_add = target_distance - starting_distance
    weeks_needed = total_distance_to_add / distance_increase_per_week
    result = weeks_needed
    return result

print(solution())