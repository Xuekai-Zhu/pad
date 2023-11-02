def solution():
    # Convert the measurements to inches
    height_in_inches = 10 * 12  # 10 feet tall, each foot has 12 inches
    length_in_inches = 15 * 12  # 15 feet long, each foot has 12 inches

    # Calculate the total number of tiles needed
    tiles_needed = (height_in_inches * length_in_inches) / (1 * 1)  # each tile is 1 inch square
    result = tiles_needed
    return result

print(solution())