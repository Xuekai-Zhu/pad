def solution():
    total_tickets = 100
    jude_tickets = 16

    # Calculate the number of tickets sold by Andrea
    andrea_tickets = 2 * jude_tickets

    # Calculate the number of tickets sold by Sandra
    sandra_tickets = (jude_tickets / 2) + 4

    # Calculate the total number of tickets sold
    total_sold = jude_tickets + andrea_tickets + sandra_tickets

    # Calculate the number of tickets that still need to be sold
    tickets_left = total_tickets - total_sold
    result = tickets_left
    return result

print(solution())