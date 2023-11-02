def solution():
    # Define the speed of the horse and the bullet
    horse_speed = 20
    bullet_speed = 400

    # Calculate the relative speed of the bullet in the same direction as the horse
    bullet_relative_speed_same_direction = bullet_speed - horse_speed

    # Calculate the relative speed of the bullet in the opposite direction of the horse
    bullet_relative_speed_opposite_direction = bullet_speed + horse_speed

    # Calculate the difference in speeds
    difference_in_speeds = bullet_relative_speed_same_direction - bullet_relative_speed_opposite_direction
    result = difference_in_speeds
    return result

print(solution())