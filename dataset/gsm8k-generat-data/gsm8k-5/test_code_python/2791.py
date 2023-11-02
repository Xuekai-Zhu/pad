def solution():
    num_adults = 1  # Violet's family has 1 adult
    num_children = 6  # Violet's family has 6 children
    adult_ticket_cost = 35  # Adult tickets cost $35
    child_ticket_cost = 20  # Children's tickets cost $20

    # Calculate the total cost of individual tickets
    total_cost = (num_adults * adult_ticket_cost) + (num_children * child_ticket_cost)

    result = total_cost
    return result

print(solution())