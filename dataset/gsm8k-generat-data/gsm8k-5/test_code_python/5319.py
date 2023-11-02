def solution():
    total_people = 400 + 200  # 400 adults and 200 children go to the show
    cost_of_child_ticket = x  # Let x be the cost of a child's ticket
    cost_of_adult_ticket = 2 * x  # An adult's ticket is twice the cost of a child's ticket
    total_cost = 16000  # The total amount collected is $16,000

    # Use the information above to set up two equations:
    # Equation 1: 400 * cost_of_adult_ticket + 200 * cost_of_child_ticket = total_cost
    # Equation 2: cost_of_adult_ticket = 2 * cost_of_child_ticket
    # We can simplify equation 1 by substituting equation 2:
    # 400 * (2 * cost_of_child_ticket) + 200 * cost_of_child_ticket = total_cost
    # Solving for cost_of_child_ticket:
    cost_of_child_ticket = total_cost / 1000  # $80
    cost_of_adult_ticket = 2 * cost_of_child_ticket  # $160
    result = cost_of_adult_ticket
    return result

print(solution())