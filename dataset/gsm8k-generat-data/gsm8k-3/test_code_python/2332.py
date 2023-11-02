def solution():
    """A volcano erupts and spews ash into the sky. The ash cloud spreads out in a diameter eighteen times as far as the distance it shot up into the sky. If the ashes erupted three hundred feet into the sky, what was the radius of the ash cloud in feet?"""
    # Define the ratio of the diameter to the distance the ashes shot up
    DIAMETER_RATIO = 18

    # Define the distance the ashes shot up
    ash_shot_up = 300

    # Calculate the diameter of the ash cloud
    diameter = ash_shot_up * DIAMETER_RATIO

    # Calculate the radius of the ash cloud
    radius = diameter / 2

    # Display the radius of the ash cloud
    result = radius
    return result

print(solution())