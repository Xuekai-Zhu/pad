def solution():
    """Colin can skip at six times the speed that Brandon can. Brandon can skip at one-third the speed that Tony can. And Tony can skip at twice the speed that Bruce can. At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?"""
    bruce_speed = 1
    tony_speed = 2 * bruce_speed
    brandon_speed = 1/3 * tony_speed
    colin_speed = 6 * brandon_speed
    # convert speed units from miles per minute to miles per hour
    colin_speed = colin_speed * 60
    result = colin_speed
    return result

print(solution())