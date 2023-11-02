def solution():
    wall_height_in_inches = 10 * 12  # Convert wall height from feet to inches
    wall_length_in_inches = 15 * 12  # Convert wall length from feet to inches

    # Calculate the total number of tiles needed
    total_tiles = (wall_height_in_inches * wall_length_in_inches) / (1**2)

    result = total_tiles
    return result

print(solution())