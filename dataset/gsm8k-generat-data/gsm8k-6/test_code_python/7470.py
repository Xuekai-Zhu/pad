def solution():
    # Calculate the speed at which Tony can skip
    tony_speed = 2  # Bruce skips at 1 mile per hour, so Tony can skip at twice that speed

    # Calculate the speed at which Brandon can skip
    brandon_speed = tony_speed / 3  # Brandon can skip at one-third the speed of Tony

    # Calculate the speed at which Colin can skip
    colin_speed = 6 * brandon_speed  # Colin can skip at six times the speed of Brandon

    # Convert Colins' speed from miles per hour to centimeters per minute
    colin_speed_cm_per_min = colin_speed * 1609.34 / 60  # 1 mile = 1609.34 meters, and 1 hour = 60 minutes

    result = colin_speed_cm_per_min
    return result

print(solution())