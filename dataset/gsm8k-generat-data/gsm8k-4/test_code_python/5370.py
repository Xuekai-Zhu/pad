def solution():
    """If a circle has a radius of 14 feet, how many 6-inch pencils can be placed end-to-end across the diameter of the circle?"""
    # Define the radius of the circle
    radius = 14

    # Calculate the diameter of the circle
    diameter = radius * 2

    # Convert the diameter from feet to inches
    diameter_inches = diameter * 12

    # Calculate the number of pencils that can fit end-to-end across the diameter
    pencil_length = 6
    pencils_fit = diameter_inches // pencil_length

    # return the result
    result = pencils_fit
    return result

print(solution())