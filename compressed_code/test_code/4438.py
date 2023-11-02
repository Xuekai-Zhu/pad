def solution():
    
    olivia_money = 112
    nigel_money = 139
    total_money = olivia_money + nigel_money
    ticket_price = 28
    num_tickets = 6
    total_cost = ticket_price * num_tickets
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())