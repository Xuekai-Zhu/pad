def solution():
    bruce_speed = 1
    tony_speed = bruce_speed * 2
    brandon_speed = tony_speed * (1/3)
    colin_speed = brandon_speed * 6

    # Convert Colin's speed from miles per minute to miles per hour
    colin_speed *= 60

    result = colin_speed
    return result

print(solution())