def solution():
    total_cost = 720
    adult_ticket_price = 15
    child_ticket_price = 8
    adult_ticket_count = total_cost // adult_ticket_price
    child_ticket_count = adult_ticket_count - 25
    total_ticket_count = adult_ticket_count + child_ticket_count
    result = child_ticket_count
    
    return result

print(solution())