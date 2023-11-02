def solution():
    # Convert the radius from feet to inches
    radius = 14 * 12

    # Calculate the diameter of the circle in inches
    diameter = 2 * radius

    # Convert the pencil length from inches to feet
    pencil_length = 6 / 12

    # Calculate how many pencils can fit end-to-end across the diameter of the circle
    pencils_across_diameter = diameter / pencil_length

    result = pencils_across_diameter
    return result

print(solution())