def solution():
    meal_cost = 10  # Kim orders a $10 meal
    drink_cost = 2.5  # Kim orders a drink for $2.5
    total_cost = meal_cost + drink_cost  # Calculate the total cost of the meal and drink
    tip_percent = 20  # Kim gives a 20% tip
    tip_amount = total_cost * (tip_percent / 100)  # Calculate the tip amount
    total_paid = total_cost + tip_amount  # Calculate the total amount Kim paid
    amount_paid_with = 20  # Kim pays with a $20 bill

    # Calculate the change Kim receives
    change = amount_paid_with - total_paid
    result = change
    return result

print(solution())