def solution():
    # Define Tate's original number of tickets
    tate_tickets = 32

    # Add the two tickets he buys
    tate_tickets += 2

    # Calculate Peyton's number of tickets
    peyton_tickets = tate_tickets / 2

    # Calculate the total number of tickets
    total_tickets = tate_tickets + peyton_tickets

    result = total_tickets
    return result

print(solution())