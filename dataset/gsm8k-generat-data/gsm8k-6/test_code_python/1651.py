def solution():
    # Calculate the internal dimensions of the box
    internal_length = 26 - 2*1  # the walls are 1 inch thick on each side
    internal_width = 26 - 2*1
    internal_height = 14 - 2*1

    # Calculate the internal volume in cubic inches and convert to cubic feet
    cubic_inches = internal_length * internal_width * internal_height
    cubic_feet = cubic_inches / 12**3
    result = cubic_feet
    return result

print(solution())