def solution():
    adult_ticket_price = 30
    child_ticket_price = adult_ticket_price / 2
    group_size = 10
    num_children = 4
    num_adults = group_size - num_children
    soda_price = 5

    # Calculate the total cost of admission before the soda discount
    total_admission_cost = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)

    # Apply the soda discount
    total_admission_cost *= 0.8

    # Add the cost of the soda
    total_cost = total_admission_cost + soda_price
    result = total_cost
    return result

print(solution())