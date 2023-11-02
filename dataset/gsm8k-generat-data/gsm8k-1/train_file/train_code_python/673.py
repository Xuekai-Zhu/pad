def solution():
    """A parking garage near Nora's house is 4 stories tall. There are 100 spots per level. There are 58 open parking spots on the first level. There are 2 more open parking spots on the second level than on the first level, and there are 5 more open parking spots on the third level than on the second level. There are 31 open parking spots on the fourth level. How many full parking spots are there in all?"""
    levels = 4
    spots_per_level = 100
    open_spots = [58, 58+2, 58+2+5, 31]
    full_spots = (spots_per_level - open_spots) * levels
    result = full_spots
    return result

print(solution())