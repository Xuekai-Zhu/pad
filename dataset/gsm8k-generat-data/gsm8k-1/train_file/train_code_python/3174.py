def solution():
    """Bill is laying power cable for a new neighborhood. There are going to be 18 east-west streets that are 2 miles long and 10 north-south streets that are four miles long. It takes 5 miles of cable to electrify 1 mile of street. If cable costs $2000/mile, what is the total cost of cable for the neighborhood?"""
    num_east_west_streets = 18
    east_west_street_length = 2
    num_north_south_streets = 10
    north_south_street_length = 4
    cable_per_street = 5
    cost_per_mile = 2000
    
    total_east_west_miles = num_east_west_streets * east_west_street_length
    total_north_south_miles = num_north_south_streets * north_south_street_length
    
    total_street_miles = total_east_west_miles + total_north_south_miles
    total_cable_miles = total_street_miles * cable_per_street
    
    total_cost = total_cable_miles * cost_per_mile
    
    result = total_cost
    return result

print(solution())