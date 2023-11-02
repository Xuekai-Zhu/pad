def solution():
    """Wild Bill can shoot a pistol while riding his horse at full speed. His horse runs at 20 feet per second, and a bullet fired from his gun flies at a speed of 400 feet per second. But if he fires a gun while riding his horse, and the gun is aimed in the same direction that the horse is running, how much faster, in feet per second, is the bullet flying than if he fires the bullet in the opposite direction of what the horse was running?"""
    horse_speed = 20
    bullet_speed = 400
    relative_speed_same_direction = bullet_speed - horse_speed
    relative_speed_opposite_direction = bullet_speed + horse_speed
    speed_difference = relative_speed_same_direction - relative_speed_opposite_direction
    result = abs(speed_difference)
    return result

print(solution())