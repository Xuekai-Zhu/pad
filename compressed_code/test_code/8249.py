def solution():
    
    initial_money = 120
    hamburgers_cost = 4
    milkshakes_cost = 3
    hamburgers_bought = 8
    milkshakes_bought = 6
    total_cost = (hamburgers_cost * hamburgers_bought) + (milkshakes_cost * milkshakes_bought)
    money_left = initial_money - total_cost
    result = money_left
    return result

print(solution())