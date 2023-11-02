def solution():
    # Define the number of adults and the regular ticket price
    num_adults = 2
    regular_ticket_price = 9

    # Calculate the total amount paid by the family
    total_paid = 2 * 20 - 1

    # Calculate the amount paid for the children's tickets
    children_ticket_price = regular_ticket_price - 2
    children_ticket_total = total_paid - num_adults * regular_ticket_price
    num_children = children_ticket_total / children_ticket_price
    result = num_children
    return result

print(solution())