def solution():
    # Define the number of adult tickets sold
    adult_tickets_sold = 250 - 188

    # Calculate the revenue from adult tickets
    adult_ticket_revenue = adult_tickets_sold * 6

    # Calculate the revenue from child tickets
    child_ticket_revenue = 188 * 4

    # Calculate the total ticket revenue
    total_revenue = adult_ticket_revenue + child_ticket_revenue
    result = total_revenue
    return result

print(solution())