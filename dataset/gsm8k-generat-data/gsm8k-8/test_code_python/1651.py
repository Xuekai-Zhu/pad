def solution():
    # Calculate the internal dimensions of the box
    internal_length = 26 - 2*1
    internal_width = 26 - 2*1
    internal_height = 14 - 2*1

    # Convert inches to feet for each dimension
    internal_length_ft = internal_length / 12
    internal_width_ft = internal_width / 12
    internal_height_ft = internal_height / 12

    # Calculate the internal volume in cubic feet
    volume = internal_length_ft * internal_width_ft * internal_height_ft

    result = volume
    return result

print(solution())