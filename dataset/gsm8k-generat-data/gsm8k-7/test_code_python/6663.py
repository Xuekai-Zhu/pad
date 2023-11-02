def solution():
    horse_speed = 20
    bullet_speed = 400

    # Calculate the relative speed of the bullet to the ground when fired in the direction of the horse's run
    rel_speed_same_dir = bullet_speed - horse_speed

    # Calculate the relative speed of the bullet to the ground when fired in the opposite direction of the horse's run
    rel_speed_opposite_dir = bullet_speed + horse_speed

    # Calculate the speed difference between the two scenarios
    speed_difference = rel_speed_same_dir - rel_speed_opposite_dir
    result = speed_difference
    return result

print(solution())