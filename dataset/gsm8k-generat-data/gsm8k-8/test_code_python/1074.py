def solution():
    # Calculate the total number of tiles
    total_tiles = 10 * 20

    # Convert the total number of tiles to inches
    total_inches = total_tiles * 36

    # Convert the total inches to square feet
    square_feet = total_inches / 144
    result = square_feet
    return result

print(solution())