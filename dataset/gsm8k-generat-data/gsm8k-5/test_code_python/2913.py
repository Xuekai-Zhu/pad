def solution():
    # Calculate the number of tickets sold by Andrea
    andrea_tickets = 2 * 16  # Andrea sold twice as many tickets as Jude

    # Calculate the number of tickets sold by Sandra
    sandra_tickets = (16 / 2) + 4  # Sandra sold 4 more than half the number of tickets Jude sold

    # Calculate the total number of tickets sold 
    total_tickets = 16 + andrea_tickets + sandra_tickets

    # Calculate the number of tickets that still need to be sold
    tickets_left = 100 - total_tickets
    result = tickets_left
    return result

print(solution())