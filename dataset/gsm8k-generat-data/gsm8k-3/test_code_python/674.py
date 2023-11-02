def solution():
    """A parking garage near Nora's house is 4 stories tall. There are 100 spots per level. There are 58 open parking spots on the first level. There are 2 more open parking spots on the second level than on the first level, and there are 5 more open parking spots on the third level than on the second level. There are 31 open parking spots on the fourth level. How many full parking spots are there in all?"""
    # Define the number of levels and parking spots per level
    LEVELS = 4
    SPOTS_PER_LEVEL = 100

    # Define the number of open parking spots on each level
    open_spots_1 = 58
    open_spots_2 = open_spots_1 + 2
    open_spots_3 = open_spots_2 + 5
    open_spots_4 = 31

    # Calculate the number of full parking spots on each level
    full_spots_1 = SPOTS_PER_LEVEL - open_spots_1
    full_spots_2 = SPOTS_PER_LEVEL - open_spots_2
    full_spots_3 = SPOTS_PER_LEVEL - open_spots_3
    full_spots_4 = SPOTS_PER_LEVEL - open_spots_4

    # Calculate the total number of full parking spots
    total_full_spots = full_spots_1 + full_spots_2 + full_spots_3 + full_spots_4

    # Display the total number of full parking spots
    result = total_full_spots
    return result

print(solution())