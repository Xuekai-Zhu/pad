def solution():
    
    adult_ticket_price = 8
    child_ticket_price = 3
    total_money = 35
    max_children = (total_money - adult_ticket_price) / child_ticket_price
    result = int(max_children)
    return result

print(solution())