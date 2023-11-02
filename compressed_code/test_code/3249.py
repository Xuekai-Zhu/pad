def solution():
    
    adult_tickets = 9
    adult_price = 11
    child_tickets = 7
    child_price = 7
    adult_total = adult_tickets * adult_price
    child_total = child_tickets * child_price
    difference = adult_total - child_total
    result = difference
    return result

print(solution())