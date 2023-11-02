def solution():
    num_adults = 1
    adult_ticket_price = 35
    num_children = 6
    children_ticket_price = 20

    # Calculate the total cost of adult tickets
    total_adult_cost = num_adults * adult_ticket_price

    # Calculate the total cost of children tickets
    total_children_cost = num_children * children_ticket_price

    # Calculate the total cost of all tickets purchased separately
    total_cost_separate = total_adult_cost + total_children_cost

    result = total_cost_separate
    return result

print(solution())