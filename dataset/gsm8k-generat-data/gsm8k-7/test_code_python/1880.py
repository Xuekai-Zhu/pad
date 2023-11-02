def solution():
    cory_speed = 12 # miles per hour
    milo_speed_skateboard = cory_speed / 4 # since Milo's speed on skateboard is half that of his running speed
    milo_speed_run = milo_speed_skateboard / 2 # since Milo's running speed is half that of his skateboarding speed

    # Calculate the distance Milo can run in two hours
    distance_milo_runs = milo_speed_run * 2 # since he runs for two hours
    result = distance_milo_runs
    return result

print(solution())