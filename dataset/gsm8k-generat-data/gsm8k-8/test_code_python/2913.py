def solution():
    # Define the number of tickets Jude sold
    jude_tickets = 16
    
    # Calculate the number of tickets sold by Andrea
    andrea_tickets = 2 * jude_tickets
    
    # Calculate the number of tickets sold by Sandra
    sandra_tickets = 4 + 0.5 * jude_tickets
    
    # Calculate the total number of tickets sold
    total_tickets_sold = jude_tickets + andrea_tickets + sandra_tickets
    
    # Calculate the number of tickets left to be sold
    tickets_left = 100 - total_tickets_sold
    result = tickets_left
    return result

print(solution())