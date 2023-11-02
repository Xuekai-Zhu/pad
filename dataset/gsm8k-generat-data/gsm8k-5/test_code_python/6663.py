def solution():
    horse_speed = 20  # Horse runs at 20 feet per second
    bullet_speed = 400  # Bullet flies at a speed of 400 feet per second

    # Calculate the speed of the bullet fired in the same direction as the horse is running
    bullet_speed_same_direction = bullet_speed + horse_speed

    # Calculate the speed of the bullet fired in the opposite direction of the horse's running
    bullet_speed_opposite_direction = bullet_speed - horse_speed

    # Calculate the difference in speed between the two scenarios
    speed_difference = bullet_speed_same_direction - bullet_speed_opposite_direction
    result = speed_difference
    return result

print(solution())