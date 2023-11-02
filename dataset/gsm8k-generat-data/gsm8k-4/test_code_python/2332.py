def solution():
    """A volcano erupts and spews ash into the sky. The ash cloud spreads out in a diameter eighteen times as far as the distance it shot up into the sky. If the ashes erupted three hundred feet into the sky, what was the radius of the ash cloud in feet?"""
    # Define the distance the ashes shot up into the sky
    eruption_height = 300

    # Calculate the diameter of the ash cloud
    ash_cloud_diameter = eruption_height * 18

    # Calculate the radius of the ash cloud
    ash_cloud_radius = ash_cloud_diameter / 2

    result = ash_cloud_radius
    return result

print(solution())