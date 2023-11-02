def solution():
    # Calculate the cost for a family of 6 to enter the park
    entrance_cost = 5*6  # $5 for each person

    # Calculate the cost for one attraction
    attraction_cost = 4 + 4*2 + 2*4  # $4 for each parent, $2 for each child, and 1 grandmother is not participating

    # Calculate the total cost for the family to visit the park and one attraction
    total_cost = entrance_cost + attraction_cost
    result = total_cost
    return result

print(solution())