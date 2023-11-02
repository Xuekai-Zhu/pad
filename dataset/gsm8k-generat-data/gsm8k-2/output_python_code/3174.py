def solution():
    """Bill is laying power cable for a new neighborhood. There are going to be 18 east-west streets that are 2 miles long and 10 north-south streets that are four miles long. It takes 5 miles of cable to electrify 1 mile of street. If cable costs $2000/mile, what is the total cost of cable for the neighborhood?"""
    east_west_streets = 18
    east_west_length = 2
    north_south_streets = 10
    north_south_length = 4
    cable_ratio = 5
    cable_cost = 2000
    total_east_west_cable = east_west_streets * east_west_length * cable_ratio
    total_north_south_cable = north_south_streets * north_south_length * cable_ratio
    total_cable_length = total_east_west_cable + total_north_south_cable
    total_cable_cost = total_cable_length / cable_ratio * cable_cost
    result = total_cable_cost
    return result

print(solution())