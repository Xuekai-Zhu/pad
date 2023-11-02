def solution():
    
    ticket_cost = 100 * 2
    dinner_cost = 120
    tip_percent = 30
    tip_cost = dinner_cost * (tip_percent / 100)
    limo_cost = 80 * 6
    total_cost = ticket_cost + dinner_cost + tip_cost + limo_cost
    result = total_cost
    return result

print(solution())