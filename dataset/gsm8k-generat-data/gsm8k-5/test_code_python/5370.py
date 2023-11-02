def solution():
    radius = 14  # Radius of the circle is 14 feet
    diameter = 2 * radius  # Diameter of the circle is twice the radius
    diameter_inches = diameter * 12  # Convert diameter to inches
    pencil_length = 6  # Length of each pencil is 6 inches

    # Calculate how many pencils can be placed end-to-end across the diameter
    pencils_across_diameter = diameter_inches / pencil_length
    result = pencils_across_diameter
    return result

print(solution())