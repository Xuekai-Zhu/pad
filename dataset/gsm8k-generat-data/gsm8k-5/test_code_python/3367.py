def solution():
    # Calculate the number of adult attendees
    num_adults = 250 - 188  # Subtract the number of children from the total seats

    # Calculate the total revenue from adult tickets
    adult_ticket_price = 6  # Cost of a ticket for an adult
    adult_revenue = num_adults * adult_ticket_price

    # Calculate the total revenue from child tickets
    child_ticket_price = 4  # Cost of a ticket for a child
    child_revenue = 188 * child_ticket_price

    # Calculate the total ticket revenue for this movie session
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())