def solution():
    cost_of_meal = 10
    cost_of_drink = 2.5
    tip_percent = 20
    total_cost = cost_of_meal + cost_of_drink
    tip_amount = total_cost * (tip_percent / 100)
    total_bill = total_cost + tip_amount
    amount_paid = 20
    change_due = amount_paid - total_bill
    result = change_due
    return result

print(solution())