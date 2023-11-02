def solution():
    # Calculate the total area of each wall
    wall_area = 2 * (20 * 8) + 2 * (20 * 8) + 2 * (20 * 8)  # each wall is 20 feet wide by 8 feet tall
    # Subtract the area of the doorways and window
    wall_area -= 3 * 7  # area of first doorway
    wall_area -= 6 * 4  # area of window
    wall_area -= 5 * 7  # area of closet doorway
    result = wall_area
    return result

print(solution())