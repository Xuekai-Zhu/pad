def solution():
    cost_burger = 3
    cost_milkshake = 5
    cost_cheese_fries = 8
    total_cost = cost_burger + cost_milkshake + cost_cheese_fries
    percent_to_pay = 80
    money_paid = total_cost * (percent_to_pay / 100)
    money_left = total_cost - money_paid
    jims_money = 20
    coussins_money = money_left - jims_money
    result = coussins_money
    
    return result

print(solution())