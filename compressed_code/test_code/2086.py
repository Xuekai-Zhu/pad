def solution():
    
    adult_tickets = 10
    child_tickets = 11
    total_bill = 124
    adult_ticket_price = 8
    child_ticket_price = (total_bill - (adult_tickets * adult_ticket_price)) / child_tickets
    result = child_ticket_price
    return result

print(solution())