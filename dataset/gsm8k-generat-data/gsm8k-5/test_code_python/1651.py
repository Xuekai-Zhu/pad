def solution():
    # Calculate the internal dimensions of the box
    internal_length = 26 - 2*1  # 1 inch thick walls on both sides, so subtract 2 inches
    internal_width = 26 - 2*1
    internal_height = 14 - 2*1

    # Calculate the volume of the box in cubic inches
    volume_in_cubic_inches = internal_length * internal_width * internal_height

    # Convert the volume to cubic feet
    volume_in_cubic_feet = volume_in_cubic_inches / 1728

    result = volume_in_cubic_feet
    return result

print(solution())