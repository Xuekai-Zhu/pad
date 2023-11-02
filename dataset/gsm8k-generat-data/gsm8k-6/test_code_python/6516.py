def solution():
    # Calculate Tate's total number of tickets after buying two more
    tate_tickets = 32 + 2
    
    # Calculate Peyton's total number of tickets
    peyton_tickets = tate_tickets / 2
    
    # Calculate the total number of tickets Tate and Peyton have together
    total_tickets = tate_tickets + peyton_tickets
    
    result = total_tickets
    return result

print(solution())