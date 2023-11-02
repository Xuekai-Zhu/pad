def solution():
    
    meal_cost = 10
    drink_cost = 2.5
    tip_percent = 20
    total_cost = meal_cost + drink_cost
    tip_amount = total_cost * (tip_percent / 100)
    total_with_tip = total_cost + tip_amount
    payment = 20
    change = payment - total_with_tip
    result = change
    return result

print(solution())