def solution():
    # Define the ticket prices
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9

    # Calculate the number of tickets needed for each age group
    num_adult_tickets = 2  # For Mrs. Lopez and her husband
    num_child_tickets = 3  # For her three children
    num_senior_tickets = 2  # For her parents

    # Calculate the total cost of the tickets
    total_cost = (num_adult_tickets * adult_ticket_price) + (num_child_tickets * child_ticket_price) + (num_senior_tickets * senior_ticket_price)

    result = total_cost
    return result

print(solution())