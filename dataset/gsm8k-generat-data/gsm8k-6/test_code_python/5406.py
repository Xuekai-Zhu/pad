def solution():
    # Define variable names
    c = child_ticket_cost
    a = adult_ticket_cost

    # Set up equations
    eq1 = a - c == 6  # the cost of an adult ticket is $6 more than the cost of a child ticket
    eq2 = 3*c + 2*a == 77  # the total cost of the 5 tickets is $77

    # Solve the system of equations
    solution = solve((eq1, eq2), (c, a))
    adult_ticket_cost = solution[1]  # get the solution for the adult ticket cost
    result = adult_ticket_cost
    return result

print(solution())