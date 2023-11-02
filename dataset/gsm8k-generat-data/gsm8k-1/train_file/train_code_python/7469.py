def solution():
    """Colin can skip at six times the speed that Brandon can. Brandon can skip at one-third the speed that Tony can. And Tony can skip at twice the speed that Bruce can. At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?"""
    bruce_speed = 1
    tony_speed = bruce_speed * 2
    brandon_speed = tony_speed / 3
    colin_speed = brandon_speed * 6
    colin_speed_in_mph = colin_speed * 2.237
    result = colin_speed_in_mph
    return result

print(solution())