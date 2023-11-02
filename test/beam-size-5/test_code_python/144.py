def solution():
    
    adult_ticket_cost = 12
    child_ticket_cost = 10
    total_cost = (adult_ticket_cost * 1) + (child_ticket_cost * 1) + (adult_ticket_cost * 1)
    change = 8
    money_given = total_cost - change
    result = money_given
    return result

print(solution())