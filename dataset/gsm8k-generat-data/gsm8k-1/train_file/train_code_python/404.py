def solution():
    """A river is to be used for a boat race. If each boat is 3 feet across and they must have at least 2 feet between them or the riverbank, how many boats can race in a river that is 42 feet across?"""
    river_width = 42
    boat_width = 3
    space_between_boats = 2
    total_space_needed = boat_width + space_between_boats
    max_boats = (river_width - 2 * space_between_boats) // total_space_needed
    result = max_boats
    return result

print(solution())