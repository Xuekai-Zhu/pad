def solution():
    bruce_speed = 1  # Bruce can skip at 1 mile per hour
    tony_speed = 2 * bruce_speed  # Tony can skip at twice Bruce's speed
    brandon_speed = tony_speed / 3  # Brandon can skip at one-third Tony's speed
    colin_speed = 6 * brandon_speed  # Colin can skip at six times Brandon's speed
    result = colin_speed
    return result

print(solution())