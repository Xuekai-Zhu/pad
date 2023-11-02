def solution():
    max_capacity = 50
    ticket_price = 8
    tickets_sold = 24
    tickets_not_sold = max_capacity - tickets_sold
    revenue = ticket_price * tickets_sold
    result = revenue - (ticket_price * max_capacity)
    return result

print(solution())