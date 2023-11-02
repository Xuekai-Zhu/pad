def solution():
    """Wild Bill can shoot a pistol while riding his horse at full speed.  His horse runs at 20 feet per second, and a bullet fired from his gun flies at a speed of 400 feet per second.  But if he fires a gun while riding his horse, and the gun is aimed in the same direction that the horse is running, how much faster, in feet per second, is the bullet flying than if he fires the bullet in the opposite direction of what the horse was running?"""
    # Define the speed of Bill's horse and the speed of the bullet
    HORSE_SPEED = 20
    BULLET_SPEED = 400

    # Calculate the relative speed of the bullet when fired in the same direction as the horse
    same_direction_speed = BULLET_SPEED - HORSE_SPEED

    # Calculate the relative speed of the bullet when fired in the opposite direction as the horse
    opposite_direction_speed = BULLET_SPEED + HORSE_SPEED

    # Calculate the difference in speed between the two scenarios
    speed_difference = same_direction_speed - opposite_direction_speed

    # Display the speed difference
    result = speed_difference
    return result

print(solution())