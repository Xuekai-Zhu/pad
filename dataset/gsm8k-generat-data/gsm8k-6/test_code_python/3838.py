def solution():
    meal_cost = 10  # cost of the meal
    drink_cost = 2.5  # cost of the drink
    subtotal = meal_cost + drink_cost  # subtotal before tip
    tip = subtotal * 0.2  # 20% tip
    total = subtotal + tip  # total cost including tip
    paid_with = 20  # amount paid by Kim
    change = paid_with - total  # amount of change
    result = change
    return result

print(solution())