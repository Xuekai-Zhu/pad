def solution():
    # Define ticket prices
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9

    # Calculate the cost of tickets for Mrs. Lopez and her husband
    adult_tickets = 2  # Mrs. Lopez and her husband are both adults
    adult_ticket_cost = adult_tickets * adult_ticket_price

    # Calculate the cost of tickets for Mrs. Lopez's parents
    senior_tickets = 2  # Mrs. Lopez's parents are both seniors
    senior_ticket_cost = senior_tickets * senior_ticket_price

    # Calculate the cost of tickets for Mrs. Lopez's children
    child_tickets = 3
    child_ticket_cost = child_tickets * child_ticket_price

    # Calculate the total cost of tickets
    total_cost = adult_ticket_cost + senior_ticket_cost + child_ticket_cost
    result = total_cost
    return result

print(solution())