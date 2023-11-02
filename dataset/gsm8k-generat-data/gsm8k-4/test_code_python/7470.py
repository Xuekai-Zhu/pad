def solution():
    """Colin can skip at six times the speed that Brandon can. Brandon can skip at one-third the speed that Tony can. And Tony can skip at twice the speed that Bruce can. At what speed, in miles per hour, can Colin skip if Bruce skips at 1 mile per hour?"""
    # Define the skipping speed of Bruce
    bruce_speed = 1

    # Calculate the skipping speed of Tony
    tony_speed = bruce_speed * 2

    # Calculate the skipping speed of Brandon
    brandon_speed = tony_speed / 3

    # Calculate the skipping speed of Colin
    colin_speed = brandon_speed * 6

    # Convert the skipping speed of Colin to miles per hour
    colin_speed_mph = colin_speed * 0.0568182

    # Round the skipping speed of Colin to two decimal places
    result = round(colin_speed_mph, 2)
    return result

print(solution())