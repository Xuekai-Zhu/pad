def solution():
    lumber_cost = 450  # initial cost of lumber
    nails_cost = 30  # initial cost of nails
    fabric_cost = 80  # initial cost of fabric

    # Calculate the new cost after inflation
    new_lumber_cost = lumber_cost * 1.2  
    new_nails_cost = nails_cost * 1.1  
    new_fabric_cost = fabric_cost * 1.05  

    # Calculate the difference in cost
    difference = (new_lumber_cost + new_nails_cost + new_fabric_cost) - (lumber_cost + nails_cost + fabric_cost)
    result = difference
    return result

print(solution())