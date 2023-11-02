def solution():
    ticket_price = 40
    num_tickets = 12

    if num_tickets > 10:
        total_price = (10 * ticket_price) + ((num_tickets - 10) * (ticket_price * 0.95))
    else:
        total_price = num_tickets * ticket_price

    result = total_price
    return result

print(solution())