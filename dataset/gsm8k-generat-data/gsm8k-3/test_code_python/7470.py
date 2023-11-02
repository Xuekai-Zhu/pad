def solution():
    """Colin can skip at six times the speed that Brandon can.  Brandon can skip at one-third the speed that Tony can.  And Tony can skip at twice the speed that Bruce can.  At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?"""
    # Calculate Bruce's skipping speed
    bruce_speed = 1

    # Calculate Tony's skipping speed
    tony_speed = 2 * bruce_speed

    # Calculate Brandon's skipping speed
    brandon_speed = 1/3 * tony_speed

    # Calculate Colin's skipping speed
    colin_speed = 6 * brandon_speed

    # Display Colin's skipping speed in miles per hour
    result = colin_speed
    return result

print(solution())