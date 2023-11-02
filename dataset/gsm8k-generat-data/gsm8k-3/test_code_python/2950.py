def solution():
    """A parking area near Peter's house is 4 stories tall. There are 4 open parking spots on the first level. There are 7 more open parking spots on the second level than on the first level, and there are 6 more open parking spots on the third level than on the second level. There are 14 open parking spots on the fourth level. How many open parking spots are there in all?"""
    # Define the number of open parking spots on each level
    level_1_spots = 4
    level_2_spots = level_1_spots + 7
    level_3_spots = level_2_spots + 6
    level_4_spots = 14

    # Calculate the total number of open parking spots
    total_spots = level_1_spots + level_2_spots + level_3_spots + level_4_spots

    # Display the total number of open parking spots
    result = total_spots
    return result

print(solution())