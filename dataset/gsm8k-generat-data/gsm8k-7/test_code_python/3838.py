def solution():
    meal_cost = 10
    drink_cost = 2.5
    tip_percent = 0.2
    payment = 20

    # Calculate the total cost of the meal and the drink
    total_cost = meal_cost + drink_cost

    # Calculate the amount of the tip
    tip_amount = total_cost * tip_percent

    # Calculate the total amount to be paid
    total_payment = total_cost + tip_amount

    # Calculate the amount of change
    change = payment - total_payment
    result = change
    return result

print(solution())