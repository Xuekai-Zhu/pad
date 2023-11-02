def solution():
    """A parking garage near Nora's house is 4 stories tall. There are 100 spots per level. There are 58 open parking spots on the first level. There are 2 more open parking spots on the second level than on the first level, and there are 5 more open parking spots on the third level than on the second level. There are 31 open parking spots on the fourth level. How many full parking spots are there in all?"""
    spots_per_level = 100
    first_level_open_spots = 58
    second_level_open_spots = first_level_open_spots + 2
    third_level_open_spots = second_level_open_spots + 5
    fourth_level_open_spots = 31
    total_open_spots = first_level_open_spots + second_level_open_spots + third_level_open_spots + fourth_level_open_spots
    total_full_spots = (4 * spots_per_level) - total_open_spots
    result = total_full_spots
    return result

print(solution())