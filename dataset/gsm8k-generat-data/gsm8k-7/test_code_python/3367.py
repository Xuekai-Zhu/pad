def solution():
    num_adults = 250 - 188
    adult_ticket_price = 6
    child_ticket_price = 4

    # Calculate the total revenue from adult tickets
    adult_revenue = num_adults * adult_ticket_price

    # Calculate the total revenue from child tickets
    child_revenue = 188 * child_ticket_price

    # Calculate the total ticket revenue
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())