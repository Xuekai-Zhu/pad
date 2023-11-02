def solution():
    river_width = 42
    boat_width = 3
    minimum_space = 2

    # Calculate the total width taken up by one boat and the required spacing
    total_width_per_boat = boat_width + minimum_space

    # Calculate the number of boats that can fit in the river
    num_boats = (river_width - 2 * minimum_space) // total_width_per_boat

    result = num_boats
    return result

print(solution())