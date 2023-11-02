def solution():
    num_adults = 2
    adult_ticket_price = 9

    child_ticket_price = adult_ticket_price - 2

    total_money_given = 2 * 20 + 1

    # Calculate the total cost of adult tickets
    total_adult_cost = num_adults * adult_ticket_price

    # Calculate the cost of all tickets
    total_cost = total_money_given - total_adult_cost

    # Calculate the number of child tickets
    num_child_tickets = total_cost / child_ticket_price

    # Round down the number of child tickets to the nearest integer
    num_children = int(num_child_tickets)

    result = num_children
    return result

print(solution())