def solution():
    pizzas_needed = 14 / 3
    pizza_cost = 12
    babysitting_money = 4
    money_needed = pizzas_needed * pizza_cost
    babysitting_nights = money_needed / babysitting_money
    result = babysitting_nights
    
    return result

print(solution())