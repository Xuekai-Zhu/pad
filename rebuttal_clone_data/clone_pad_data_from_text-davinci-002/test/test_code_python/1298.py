def solution():
     adult_ticket_price = 4.25 + 3.25
     child_ticket_price = 4.25
     discount = 2
     total_price = (adult_ticket_price * 2) + (child_ticket_price * 4) - discount
     result = total_price
     return result

print(solution())