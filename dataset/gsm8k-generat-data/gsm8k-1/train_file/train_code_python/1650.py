def solution():
    """John builds a box. The box is 26 inches by 26 inches by 14 inches. The walls are 1 inch thick on each side. How much is the internal volume in cubic feet?"""
    length = 26
    width = 26
    height = 14
    wall_thickness = 1
    internal_length = length - 2*wall_thickness
    internal_width = width - 2*wall_thickness
    internal_height = height - 2*wall_thickness
    cubic_inches = internal_length * internal_width * internal_height
    cubic_feet = cubic_inches / 1728.0
    result = cubic_feet
    return result

print(solution())