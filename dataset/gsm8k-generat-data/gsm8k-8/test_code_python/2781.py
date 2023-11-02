def solution():
    # Define Patrick's time
    patrick_time = 60

    # Define Manu's time
    manu_time = patrick_time + 12

    # Define Amy's speed ratio to Manu
    amy_to_manu_ratio = 2

    # Calculate Manu's time
    manu_distance = patrick_time
    manu_speed = manu_distance / manu_time
    manu_distance = amy_to_manu_ratio * manu_distance
    manu_time = manu_distance / manu_speed

    # Calculate Amy's time
    amy_distance = manu_distance
    amy_speed = amy_distance / manu_time
    amy_time = amy_distance / amy_speed

    result = amy_time
    return result

print(solution())