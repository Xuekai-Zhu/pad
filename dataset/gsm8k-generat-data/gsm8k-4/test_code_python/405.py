def solution():
    """A river is to be used for a boat race. If each boat is 3 feet across and they must have at least 2 feet between them or the riverbank, how many boats can race in a river that is 42 feet across?"""
    # Define the width of each boat and the minimum space required between boats
    boat_width = 3
    min_space = 2

    # Define the width of the river
    river_width = 42

    # Calculate the available space for boats
    available_space = river_width - 2 * min_space

    # Calculate the maximum number of boats that can race
    max_boats = available_space // boat_width

    # Return the result
    result = max_boats
    return result

print(solution())