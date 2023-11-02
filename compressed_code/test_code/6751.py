def solution():
    
    initial_money = 20
    socks_cost = 2
    pairs_of_socks = 4
    hat_cost = 7
    total_cost = (socks_cost * pairs_of_socks) + hat_cost
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())