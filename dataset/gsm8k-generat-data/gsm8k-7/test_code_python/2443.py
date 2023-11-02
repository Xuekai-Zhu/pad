def solution():
    num_adults = 1  # Mary
    num_children = 3
    adult_ticket_price = 2
    child_ticket_price = 1
    total_tickets_cost = (num_adults * adult_ticket_price) + (num_children * child_ticket_price)
    amount_paid = 20
    change = amount_paid - total_tickets_cost
    result = change
    return result

print(solution())