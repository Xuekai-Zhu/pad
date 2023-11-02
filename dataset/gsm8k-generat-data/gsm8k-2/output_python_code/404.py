def solution():
    """A river is to be used for a boat race. If each boat is 3 feet across and they must have at least 2 feet between them or the riverbank, how many boats can race in a river that is 42 feet across?"""
    boat_width = 3
    min_space = 2
    river_width = 42
    available_space = river_width - (2 * min_space)
    num_boats = available_space // boat_width
    result = num_boats
    return result

print(solution())