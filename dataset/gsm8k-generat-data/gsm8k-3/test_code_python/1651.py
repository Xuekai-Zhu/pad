def solution():
    """John builds a box.  The box is 26 inches by 26 inches by 14 inches.  The walls are 1 inch thick on each side.  How much is the internal volume in cubic feet?"""
    # Define the dimensions of the box (in inches)
    length = 26
    width = 26
    height = 14

    # Define the thickness of the walls (in inches)
    wall_thickness = 1

    # Calculate the internal dimensions of the box (in inches)
    internal_length = length - 2 * wall_thickness
    internal_width = width - 2 * wall_thickness
    internal_height = height - 2 * wall_thickness

    # Calculate the internal volume of the box (in cubic inches)
    internal_volume = internal_length * internal_width * internal_height

    # Convert the internal volume to cubic feet
    cubic_feet_conversion = 1 / 1728
    internal_volume_cubic_feet = internal_volume * cubic_feet_conversion

    # Display the internal volume in cubic feet
    result = internal_volume_cubic_feet
    return result

print(solution())