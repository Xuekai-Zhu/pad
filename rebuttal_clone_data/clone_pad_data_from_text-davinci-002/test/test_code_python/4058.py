def solution():
    initial_money = 40
    pizza_cost = 2.75
    soda_cost = 1.50
    jeans_cost = 11.50
    money_spent = pizza_cost + soda_cost + jeans_cost
    quarters = (initial_money - money_spent) * 4
    result = quarters
    return result

print(solution())