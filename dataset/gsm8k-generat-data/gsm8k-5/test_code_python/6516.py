def solution():
    tate_tickets = 32  # Tate has 32 tickets
    tate_tickets += 2  # Tate buys 2 more tickets, making a total of 34 tickets
    peyton_tickets = tate_tickets / 2  # Peyton has half as many tickets as Tate

    # Calculate the total number of tickets Tate and Peyton have together
    total_tickets = tate_tickets + peyton_tickets
    result = total_tickets
    return result

print(solution())