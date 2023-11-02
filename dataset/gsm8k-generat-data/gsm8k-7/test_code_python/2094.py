def solution():
    num_adults = 2
    adult_ticket_price = 22

    num_children = 2
    child_ticket_price = 7

    # Calculate the total cost of adult tickets
    total_adult_cost = num_adults * adult_ticket_price

    # Calculate the total cost of child tickets
    total_child_cost = num_children * child_ticket_price

    # Calculate the total cost for admission
    total_cost = total_adult_cost + total_child_cost
    result = total_cost
    return result

print(solution())