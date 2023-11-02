def solution():
    """A parking area near Peter's house is 4 stories tall. There are 4 open parking spots on the first level. There are 7 more open parking spots on the second level than on the first level, and there are 6 more open parking spots on the third level than on the second level. There are 14 open parking spots on the fourth level. How many open parking spots are there in all?"""
    first_level_spots = 4
    second_level_spots = first_level_spots + 7
    third_level_spots = second_level_spots + 6
    fourth_level_spots = 14
    total_spots = first_level_spots + second_level_spots + third_level_spots + fourth_level_spots
    result = total_spots
    return result

print(solution())