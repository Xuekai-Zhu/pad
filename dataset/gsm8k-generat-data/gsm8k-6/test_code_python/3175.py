def solution():
    # Calculate the total length of east-west streets
    length_ew_streets = 18 * 2

    # Calculate the total length of north-south streets
    length_ns_streets = 10 * 4

    # Calculate the total length of streets that need to be electrified
    length_electrified = length_ew_streets + length_ns_streets

    # Calculate the total length of cable needed
    length_cable = length_electrified * 5

    # Calculate the total cost of cable
    cost_cable = length_cable * 2000

    result = cost_cable
    return result

print(solution())