def solution():
    
    starting_money = 2000
    goods_cost = 600
    debtor_payment = 800
    maintenance_cost = 1200
    remaining_money = starting_money - goods_cost + debtor_payment - maintenance_cost
    result = remaining_money
    return result

print(solution())