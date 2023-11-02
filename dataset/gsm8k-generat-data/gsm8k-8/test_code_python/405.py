def solution():
    # Define the width of each boat and the required spacing
    boat_width = 3
    spacing = 2

    # Calculate the number of boats that can fit
    num_boats = (42 - 2 * spacing) // (boat_width + spacing)

    result = num_boats
    return result

print(solution())