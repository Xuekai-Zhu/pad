def solution():
    num_kids = 6  # Six kids are going to the circus
    num_adults = 2  # Two adults are going to the circus
    total_cost = 50  # The total cost of all the tickets is $50

    # Let x be the cost of one adult ticket
    # Then the cost of one kid's ticket is x/2
    # We can set up an equation based on the total cost:
    # num_kids * (x/2) + num_adults * x = total_cost
    # Simplifying, we get: 3x = total_cost
    # Solving for x, we get: x = total_cost/3
    # Therefore, the cost of one adult ticket is $50/3
    # and the cost of one kid's ticket is $25/3
    kid_ticket_cost = total_cost / (num_kids * 0.5 + num_adults)
    result = kid_ticket_cost
    return result

print(solution())