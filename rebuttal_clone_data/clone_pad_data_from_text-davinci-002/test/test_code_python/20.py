def solution():
    
    ticket_price = 40
    discount_percentage = 5
    num_tickets = 12
    num_tickets_discount = num_tickets - 10
    discount_amount = num_tickets_discount * (discount_percentage / 100) * ticket_price
    total_price = num_tickets * ticket_price - discount_amount
    result = total_price
    
    return result

print(solution())