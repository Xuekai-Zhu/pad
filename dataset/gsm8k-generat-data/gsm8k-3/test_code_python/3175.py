def solution():
    """Bill is laying power cable for a new neighborhood. There are going to be 18 east-west streets that are 2 miles long and 10 north-south streets that are four miles long. It takes 5 miles of cable to electrify 1 mile of street. If cable costs $2000/mile, what is the total cost of cable for the neighborhood?"""
    
    # Define the lengths of each type of street
    east_west_streets = 18 * 2
    north_south_streets = 10 * 4

    # Calculate the total length of streets
    total_street_length = east_west_streets + north_south_streets

    # Calculate the length of cable needed
    cable_length = total_street_length * 5

    # Calculate the total cost of cable
    cable_cost = cable_length * 2000

    result = cable_cost
    return result

print(solution())