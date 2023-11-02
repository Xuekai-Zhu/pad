def solution():
    # Define the number of open parking spots on each level
    spots_level1 = 4
    spots_level2 = spots_level1 + 7
    spots_level3 = spots_level2 + 6
    spots_level4 = 14

    # Calculate the total number of open parking spots
    total_spots = spots_level1 + spots_level2 + spots_level3 + spots_level4
    result = total_spots
    return result

print(solution())