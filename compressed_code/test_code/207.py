def solution():
    
    num_tickets = 5
    first_ticket_price = 1
    total_ticket_price = 0
    for i in range(num_tickets):
        total_ticket_price += first_ticket_price + i

    prize = total_ticket_price - 4
    result = prize
    return result

print(solution())