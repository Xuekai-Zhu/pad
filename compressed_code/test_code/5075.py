def solution():
    
    initial_money = 20
    hat_cost = 10
    pencil_cost = 2
    cookie_cost = 1.25
    total_spent = hat_cost + pencil_cost + (4 * cookie_cost)
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())