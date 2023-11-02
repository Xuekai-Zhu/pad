def solution():
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9

    num_adults = 2  # Mrs. Lopez and her husband
    num_children = 3
    num_seniors = 2  # Mrs. Lopez's parents

    # Calculate the total cost of adult tickets
    total_adult_cost = num_adults * adult_ticket_price

    # Calculate the total cost of children's tickets
    total_child_cost = num_children * child_ticket_price

    # Calculate the total cost of senior tickets
    total_senior_cost = num_seniors * senior_ticket_price

    # Calculate the total cost of all tickets
    total_cost = total_adult_cost + total_child_cost + total_senior_cost
    result = total_cost
    return result

print(solution())