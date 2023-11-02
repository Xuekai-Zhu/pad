def solution():
    num_children_tickets = 4
    child_ticket_price = 4.25

    num_adult_tickets = 2
    adult_ticket_price = child_ticket_price + 3.25

    total_tickets = num_children_tickets + num_adult_tickets

    # Apply the $2 discount if applicable
    if total_tickets > 3:
        discount = 2
    else:
        discount = 0

    # Calculate the total cost of all tickets
    total_cost = (num_children_tickets * child_ticket_price) + (num_adult_tickets * adult_ticket_price)

    # Subtract the discount from the total cost
    total_cost -= discount

    result = total_cost
    return result

print(solution())