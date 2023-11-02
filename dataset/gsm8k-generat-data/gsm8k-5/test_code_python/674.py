def solution():
    levels = 4  # Nora's parking garage has 4 levels
    spots_per_level = 100  # There are 100 spots per level

    # Calculate the number of open spots on each level
    open_spots_level1 = 58
    open_spots_level2 = open_spots_level1 + 2
    open_spots_level3 = open_spots_level2 + 5
    open_spots_level4 = 31

    # Calculate the number of full spots on each level
    full_spots_level1 = spots_per_level - open_spots_level1
    full_spots_level2 = spots_per_level - open_spots_level2
    full_spots_level3 = spots_per_level - open_spots_level3
    full_spots_level4 = spots_per_level - open_spots_level4

    # Calculate the total number of full parking spots in all levels
    total_full_spots = levels * (full_spots_level1 + full_spots_level2 + full_spots_level3 + full_spots_level4)
    result = total_full_spots
    return result

print(solution())