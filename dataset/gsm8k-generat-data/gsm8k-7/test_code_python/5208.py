def solution():
    total_cost = 720
    adult_ticket_price = 15
    child_ticket_price = 8
    num_adults = 0
    num_children = 0

    # Set up equations to solve for the number of adults and children
    # Let x be the number of children
    # Then, the number of adults is x + 25
    # The total cost equation is 15(x + 25) + 8x = 720
    # Solving for x gives x = 27

    num_children = 27
    num_adults = num_children + 25

    result = num_children
    return result

print(solution())