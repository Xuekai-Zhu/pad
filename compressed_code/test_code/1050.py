def solution():
    
    hamburgers_cost = 4
    milkshakes_cost = 5
    hamburgers_bought = 8
    milkshakes_bought = 6
    total_spent = (hamburgers_cost * hamburgers_bought) + (milkshakes_cost * milkshakes_bought)
    initial_money = total_spent + 70
    result = initial_money
    return result

print(solution())