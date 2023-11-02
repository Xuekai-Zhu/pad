def solution():
    """If a circle has a radius of 14 feet, how many 6-inch pencils can be placed end-to-end across the diameter of the circle?"""
    # Convert the radius to inches
    radius_inches = 14 * 12

    # Calculate the diameter of the circle in inches
    diameter_inches = radius_inches * 2

    # Calculate the number of 6-inch pencils that can fit across the diameter
    pencils_across = diameter_inches // 6

    # Display the result
    result = pencils_across
    return result

print(solution())