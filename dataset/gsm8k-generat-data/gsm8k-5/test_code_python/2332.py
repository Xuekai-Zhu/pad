def solution():
    eruption_height = 300  # The ashes erupted 300 feet into the sky
    cloud_diameter = 18 * eruption_height  # The ash cloud spreads out in a diameter 18 times farther than the eruption height
    cloud_radius = cloud_diameter / 2  # The radius is half of the diameter

    result = cloud_radius
    return result

print(solution())