def solution():
    length = 26
    width = 26
    height = 14
    wall_thickness = 1
    internal_length = length - (2 * wall_thickness)
    internal_width = width - (2 * wall_thickness)
    internal_height = height - (2 * wall_thickness)
    internal_volume = internal_length * internal_width * internal_height
    result = internal_volume
    return result

print(solution())