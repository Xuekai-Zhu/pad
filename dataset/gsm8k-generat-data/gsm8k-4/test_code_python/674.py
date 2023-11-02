def solution():
    """A parking garage near Nora's house is 4 stories tall. There are 100 spots per level. There are 58 open parking spots on the first level. There are 2 more open parking spots on the second level than on the first level, and there are 5 more open parking spots on the third level than on the second level. There are 31 open parking spots on the fourth level. How many full parking spots are there in all?"""
    # Define the number of parking spots per level and the number of levels
    spots_per_level = 100
    levels = 4

    # Calculate the number of open parking spots on each level
    level1_spots = 58
    level2_spots = level1_spots + 2
    level3_spots = level2_spots + 5
    level4_spots = 31

    # Calculate the number of full parking spots on each level
    level1_full_spots = spots_per_level - level1_spots
    level2_full_spots = spots_per_level - level2_spots
    level3_full_spots = spots_per_level - level3_spots
    level4_full_spots = spots_per_level - level4_spots

    # Calculate the total number of full parking spots
    total_full_spots = (level1_full_spots + level2_full_spots + level3_full_spots + level4_full_spots) * levels

    # Return the result
    result = total_full_spots
    return result

print(solution())