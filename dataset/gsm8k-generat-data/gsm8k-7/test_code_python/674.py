def solution():
    num_levels = 4
    num_spots_per_level = 100

    # Calculate the number of open spots on each level
    level1_spots = 58
    level2_spots = level1_spots + 2
    level3_spots = level2_spots + 5
    level4_spots = 31

    # Calculate the number of full spots on each level
    level1_full_spots = num_spots_per_level - level1_spots
    level2_full_spots = num_spots_per_level - level2_spots
    level3_full_spots = num_spots_per_level - level3_spots
    level4_full_spots = num_spots_per_level - level4_spots

    # Calculate the total number of full spots
    total_full_spots = (level1_full_spots + level2_full_spots +
                        level3_full_spots + level4_full_spots) * num_levels
    result = total_full_spots
    return result

print(solution())