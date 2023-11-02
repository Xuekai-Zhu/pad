def solution():
    # Calculate the total length of east-west streets
    length_east_west = 18 * 2

    # Calculate the total length of north-south streets
    length_north_south = 10 * 4

    # Calculate the total length of streets
    total_length = length_east_west + length_north_south

    # Calculate the length of cable needed
    length_of_cable = total_length * 5

    # Calculate the total cost of cable
    total_cost = length_of_cable * 2000
    result = total_cost
    return result

print(solution())