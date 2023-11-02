def solution():
    num_children = 3  # There are 3 children in the family
    total_tickets = 5  # The family bought 5 tickets in total
    total_cost = 77  # The total cost of the tickets is $77

    # Use algebra to set up and solve the equations for the cost of child tickets and adult tickets
    # Let x = cost of child ticket
    # Let x + $6 = cost of adult ticket
    # Then: num_children * x + (total_tickets - num_children) * (x + $6) = total_cost
    # Simplifying this equation gives: 3x + 2(x + $6) = $77
    # Solving for x gives: x = $7, so the cost of an adult ticket is $13

    child_cost = 7
    adult_cost = child_cost + 6
    result = adult_cost
    return result

print(solution())