def solution():
    
    gift_cost = 250
    erika_money = 155
    rick_money = gift_cost / 2
    total_money = erika_money + rick_money
    cake_cost = 25
    remaining_money = total_money - gift_cost - cake_cost
    result = remaining_money
    return result

print(solution())