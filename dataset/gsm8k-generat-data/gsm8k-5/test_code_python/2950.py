def solution():
    # Calculate the number of open parking spots on the first level
    level_1_spots = 4

    # Calculate the number of open parking spots on the second level
    level_2_spots = level_1_spots + 7

    # Calculate the number of open parking spots on the third level
    level_3_spots = level_2_spots + 6

    # Calculate the total number of open parking spots
    total_spots = level_1_spots + level_2_spots + level_3_spots + 14
     
    result = total_spots
    return result

print(solution())