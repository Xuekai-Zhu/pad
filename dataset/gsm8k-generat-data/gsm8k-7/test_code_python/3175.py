def solution():
    num_ew_streets = 18
    ew_street_length = 2

    num_ns_streets = 10
    ns_street_length = 4

    cable_efficiency = 5  # 5 miles of cable electrify 1 mile of street
    cable_cost_per_mile = 2000

    # Calculate the total length of east-west streets
    total_ew_street_length = num_ew_streets * ew_street_length

    # Calculate the total length of north-south streets
    total_ns_street_length = num_ns_streets * ns_street_length

    # Calculate the total length of streets
    total_street_length = total_ew_street_length + total_ns_street_length

    # Calculate the total length of cable needed
    total_cable_length = total_street_length / cable_efficiency

    # Calculate the total cost of cable for the neighborhood
    total_cable_cost = total_cable_length * cable_cost_per_mile
    result = total_cable_cost
    return result

print(solution())