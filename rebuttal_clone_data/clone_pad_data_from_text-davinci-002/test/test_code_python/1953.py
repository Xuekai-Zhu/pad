def solution():
    ticket_cost = 300
    hotel_cost = ticket_cost / 2
    initial_amount = 760
    amount_left = initial_amount - (ticket_cost + hotel_cost)
    result = amount_left
    return result

print(solution())