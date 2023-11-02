def solution():
    """Bill is laying power cable for a new neighborhood. There are going to be 18 east-west streets that are 2 miles long and 10 north-south streets that are four miles long. It takes 5 miles of cable to electrify 1 mile of street. If cable costs $2000/mile, what is the total cost of cable for the neighborhood?"""
    # Define the length of the east-west and north-south streets
    east_west_length = 2
    north_south_length = 4

    # Define the number of east-west and north-south streets
    east_west_streets = 18
    north_south_streets = 10

    # Calculate the total length of the streets
    total_street_length = (east_west_length * east_west_streets) + (north_south_length * north_south_streets)

    # Calculate the total length of cable needed
    total_cable_length = total_street_length * 5

    # Calculate the total cost of the cable
    cable_cost = total_cable_length * 2000

    # Return the total cost of the cable
    result = cable_cost
    return result

print(solution())