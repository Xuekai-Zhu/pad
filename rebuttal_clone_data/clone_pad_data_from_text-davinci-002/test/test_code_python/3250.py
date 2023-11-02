def solution():
    olivia_money = 112
    nigel_money = 139
    tickets = 6
    ticket_price = 28
    total_money = olivia_money + nigel_money
    total_cost = tickets * ticket_price
    money_left = total_money - total_cost
    result = money_left
    return result

print(solution())