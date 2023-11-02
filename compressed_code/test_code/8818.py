def solution():
    
    meal_cost = 10
    drink_cost = 2.5
    total_cost = meal_cost + drink_cost
    tip_percent = 20
    tip_amount = total_cost * (tip_percent / 100)
    total_paid = total_cost + tip_amount
    amount_given = 20
    change = amount_given - total_paid
    result = change
    return result

print(solution())