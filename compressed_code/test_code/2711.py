def solution():
    
    initial_money = 760
    ticket_cost = 300
    hotel_cost = ticket_cost / 2
    remaining_money = initial_money - ticket_cost - hotel_cost
    result = remaining_money
    return result

print(solution())