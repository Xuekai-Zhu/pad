def solution():
    # Calculate the speed of the bullet when fired in the same direction as the horse.
    bullet_speed_same_direction = 400 - 20  # subtract the speed of the horse (in feet per second) from the speed of the bullet (in feet per second)

    # Calculate the speed of the bullet when fired in the opposite direction as the horse.
    bullet_speed_opposite_direction = 400 + 20  # add the speed of the horse (in feet per second) to the speed of the bullet (in feet per second)

    # Calculate the difference in speed between the two scenarios.
    speed_difference = bullet_speed_same_direction - bullet_speed_opposite_direction
    result = speed_difference
    return result

print(solution())