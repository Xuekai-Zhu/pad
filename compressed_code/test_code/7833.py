def solution():
    
    initial_money = 50
    baguette_cost = 2
    water_cost = 1
    total_spent = (2 * baguette_cost) + (2 * water_cost)
    money_left = initial_money - total_spent
    result = money_left
    return result

print(solution())