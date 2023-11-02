def solution():
    ticket_cost = 5
    popcorn_cost = 0.8 * ticket_cost
    soda_cost = 0.5 * popcorn_cost
    
    num_tickets = 4
    num_popcorn = 2
    num_soda = 4
    
    # Calculate the total cost of all movie tickets
    total_ticket_cost = num_tickets * ticket_cost
    
    # Calculate the total cost of all popcorn
    total_popcorn_cost = num_popcorn * popcorn_cost
    
    # Calculate the total cost of all soda
    total_soda_cost = num_soda * soda_cost
    
    # Calculate the total cost of everything
    total_cost = total_ticket_cost + total_popcorn_cost + total_soda_cost
    result = total_cost
    return result

print(solution())