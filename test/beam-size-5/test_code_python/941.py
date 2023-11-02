def solution():
    
    distance = 20
    speed = 2
    swim_time = distance * 0.6
    remaining_distance = distance - swim_time
    island_rest_time = remaining_distance / 2
    remaining_time = remaining_distance / 2
    total_time = swim_time + island_rest_time + remaining_time
    result = total_time
    return result

print(solution())