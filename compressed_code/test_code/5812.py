def solution():
    
    ticket_price = 40
    num_tickets = 12
    discount_percent = 5
    if num_tickets > 10:
        extra_tickets = num_tickets - 10
        discount_amount = (ticket_price * discount_percent / 100) * extra_tickets
        subtotal = (ticket_price * 10) + ((num_tickets - 10) * (ticket_price - (discount_amount / extra_tickets)))
    else:
        subtotal = num_tickets * ticket_price
        
    result = subtotal
    return result

print(solution())