def solution():
    river_width = 42  # The width of the river is 42 feet
    boat_width = 3  # Each boat is 3 feet across
    clear_space = 2  # There must be at least 2 feet of space between each boat and the riverbank

    # Calculate the available width for boats and clear space
    available_width = river_width - (2 * clear_space)
    
    # Calculate the number of boats that can fit given the available width
    num_boats = available_width // boat_width
    result = num_boats
    return result

print(solution())