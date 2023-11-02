def solution():
    # Calculate the total length of east-west streets
    east_west_length = 18 * 2

    # Calculate the total length of north-south streets
    north_south_length = 10 * 4

    # Calculate the total length of all streets
    total_length = east_west_length + north_south_length

    # Calculate the total amount of cable needed
    cable_needed = total_length * 5

    # Calculate the total cost of the cable
    total_cost = cable_needed * 2000

    result = total_cost
    return result

print(solution())