def solution():
    adult_ticket_price = 26
    child_ticket_price = 13  # half of adult ticket price
    num_adults = 183
    num_children = 28

    # Calculate the total revenue from adult tickets
    adult_revenue = num_adults * adult_ticket_price

    # Calculate the total revenue from children's tickets
    child_revenue = num_children * child_ticket_price

    # Calculate the total revenue from the concert
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())