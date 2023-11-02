def solution():
    tate_tickets = 32
    additional_tickets = 2
    peyton_tickets = (tate_tickets + additional_tickets) / 2

    # Calculate the total number of tickets Tate and Peyton have together
    total_tickets = tate_tickets + additional_tickets + peyton_tickets
    result = total_tickets
    return result

print(solution())