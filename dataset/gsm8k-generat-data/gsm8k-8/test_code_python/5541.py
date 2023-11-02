def solution():
    # Define the number of adults and children
    num_adults = 5
    num_children = 2

    # Define the cost of concessions and the total cost of the trip
    concessions_cost = 12
    total_cost = 76

    # Calculate the total cost of tickets for the children
    child_tickets_cost = num_children * 7

    # Calculate the total cost of tickets for everyone
    total_ticket_cost = total_cost - concessions_cost - child_tickets_cost

    # Calculate the cost of one adult ticket
    adult_ticket_cost = total_ticket_cost / num_adults

    return adult_ticket_cost

print(solution())