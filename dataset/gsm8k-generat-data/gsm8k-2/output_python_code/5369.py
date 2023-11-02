def solution():
    """If a circle has a radius of 14 feet, how many 6-inch pencils can be placed end-to-end across the diameter of the circle?"""
    radius = 14
    diameter = 2 * radius
    pencil_length = 6 / 12  # convert inches to feet
    pencils_across_diameter = diameter / pencil_length
    result = pencils_across_diameter
    return result

print(solution())