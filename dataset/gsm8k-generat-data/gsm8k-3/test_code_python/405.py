def solution():
    """A river is to be used for a boat race. If each boat is 3 feet across and they must have at least 2 feet between them or the riverbank, how many boats can race in a river that is 42 feet across?"""
    # Define the width of each boat and the required spacing
    BOAT_WIDTH = 3
    REQUIRED_SPACE = 2

    # Define the width of the river
    river_width = 42

    # Calculate the available width for the boats
    available_width = river_width - 2 * REQUIRED_SPACE

    # Calculate the number of boats that can race
    num_boats = available_width // BOAT_WIDTH
    
    # Display the number of boats
    result = num_boats
    return result

print(solution())