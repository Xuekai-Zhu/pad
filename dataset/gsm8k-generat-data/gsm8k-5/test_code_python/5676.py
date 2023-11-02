def solution():
    tiles_per_minute = [3, 5, 10, 8]  # Don, Ken, Laura, and Kim can paint this number of tiles per minute respectively
    total_minutes = 15  # We need to calculate the total number of tiles painted in 15 minutes

    # Calculate the total number of tiles painted by each person in 15 minutes
    don_total_tiles = tiles_per_minute[0] * total_minutes
    ken_total_tiles = tiles_per_minute[1] * total_minutes
    laura_total_tiles = tiles_per_minute[2] * total_minutes
    kim_total_tiles = tiles_per_minute[3] * total_minutes

    # Add up the total number of tiles painted by everyone
    total_tiles_painted = don_total_tiles + ken_total_tiles + laura_total_tiles + kim_total_tiles
    result = total_tiles_painted
    return result

print(solution())