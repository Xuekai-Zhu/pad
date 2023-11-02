def solution():
    # Define Bruce's skipping speed in miles per minute
    bruce_speed = 1 / 60

    # Calculate Tony's skipping speed in miles per minute
    tony_speed = 2 * bruce_speed

    # Calculate Brandon's skipping speed in miles per minute
    brandon_speed = (1 / 3) * tony_speed

    # Calculate Colin's skipping speed in miles per minute
    colin_speed = 6 * brandon_speed

    # Convert Colin's skipping speed to miles per hour
    colin_speed_mph = colin_speed * 60

    result = colin_speed_mph
    return result

print(solution())