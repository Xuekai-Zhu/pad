def solution():
    total_money = 20
    hat_cost = 10
    pencil_cost = 2
    cookie_cost = 1.25
    cookies_bought = 4
    money_spent = hat_cost + pencil_cost + (cookie_cost * cookies_bought)
    money_left = total_money - money_spent
    result = money_left
    return result

print(solution())