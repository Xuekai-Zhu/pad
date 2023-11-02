def solution():
    
    total_distance = 9300
    walking_distance = 125 * 2
    remaining_distance = total_distance - walking_distance
    additional_distance_per_day = remaining_distance / 30
    result = additional_distance_per_day
    return result

print(solution())