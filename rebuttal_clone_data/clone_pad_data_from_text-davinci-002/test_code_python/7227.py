def solution():
    amount_of_money = 20
    cost_of_pencil = 1.60
    cost_of_pen = 2
    number_of_pens_desired = 6
    total_cost_of_pens = cost_of_pen * number_of_pens_desired
    money_left = amount_of_money - total_cost_of_pens
    number_of_pencils = money_left / cost_of_pencil
    result = number_of_pencils
    return result

print(solution())