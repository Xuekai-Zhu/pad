def solution():
    meal_cost = 10
    drink_cost = 2.5
    total_cost = meal_cost + drink_cost
    tip_percentage = 0.2
    tip_amount = total_cost * tip_percentage
    total_amount_due = total_cost + tip_amount
    amount_paid = 20

    change = amount_paid - total_amount_due
    result = change
    return result

print(solution())