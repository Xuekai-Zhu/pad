def solution():
    """John builds a box. The box is 26 inches by 26 inches by 14 inches. The walls are 1 inch thick on each side. How much is the internal volume in cubic feet?"""
    external_length = 26 + 2 * 1  # 1 inch thick wall on each side
    external_width = 26 + 2 * 1  # 1 inch thick wall on each side
    external_height = 14 + 2 * 1  # 1 inch thick wall on each side
    internal_length = external_length - 2 * 1  # subtract 1 inch wall thickness from length
    internal_width = external_width - 2 * 1  # subtract 1 inch wall thickness from width
    internal_height = external_height - 2 * 1  # subtract 1 inch wall thickness from height
    volume_cubic_inches = internal_length * internal_width * internal_height
    volume_cubic_feet = volume_cubic_inches / 12 / 12 / 12  # convert cubic inches to cubic feet
    result = volume_cubic_feet
    return result

print(solution())