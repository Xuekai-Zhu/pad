def solution():
    # Calculate the total number of tickets sold by all three sellers
    jude_tickets = 16
    andrea_tickets = 2 * jude_tickets
    sandra_tickets = (1/2 * jude_tickets) + 4
    total_tickets_sold = jude_tickets + andrea_tickets + sandra_tickets

    # Calculate the number of tickets that still need to be sold
    tickets_left = 100 - total_tickets_sold
    result = tickets_left
    return result

print(solution())