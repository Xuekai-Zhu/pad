def solution():
    speed_normal = 2
    speed_black_hole = 3
    hours_traveled_normal = 7
    hours_traveled_black_hole = 2
    distance_traveled_normal = hours_traveled_normal * speed_normal
    distance_traveled_black_hole = hours_traveled_black_hole * speed_black_hole
    total_distance = distance_traveled_normal + distance_traveled_black_hole
    result = total_distance
    return result

print(solution())