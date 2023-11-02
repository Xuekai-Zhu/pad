def solution():
    # Define the cost of one ticket
    ticket_cost = 44

    # Define the number of tickets Sebastian bought
    num_tickets = 3

    # Calculate the total cost of the tickets
    ticket_total_cost = ticket_cost * num_tickets

    # Add the service fee
    total_cost = ticket_total_cost + 18

    result = total_cost
    return result

print(solution())