def solution():
    
    grass_field_distance = 10
    forest_distance = 12
    total_distance_per_day = grass_field_distance + forest_distance
    total_distance_per_week = total_distance_per_day * 5
    result = total_distance_per_week
    return result

print(solution())