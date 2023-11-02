def solution():
    """Wild Bill can shoot a pistol while riding his horse at full speed. His horse runs at 20 feet per second, and a bullet fired from his gun flies at a speed of 400 feet per second. But if he fires a gun while riding his horse, and the gun is aimed in the same direction that the horse is running, how much faster, in feet per second, is the bullet flying than if he fires the bullet in the opposite direction of what the horse was running?"""
    # Calculate the relative velocity of the bullet when fired in the same direction as the horse
    relative_velocity_same = 400 - 20

    # Calculate the relative velocity of the bullet when fired in the opposite direction of the horse
    relative_velocity_opposite = 400 + 20

    # Calculate the difference in relative velocity
    velocity_difference = relative_velocity_same - relative_velocity_opposite

    result = velocity_difference
    return result

print(solution())