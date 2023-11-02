def solution():
    
    tickets_price = 7
    num_tickets = 24
    ticket_discount = 0.5
    total_price = num_tickets * tickets_price
    discounted_price = total_price * ticket_discount
    final_price = total_price - discounted_price
    result = final_price
    return result

print(solution())