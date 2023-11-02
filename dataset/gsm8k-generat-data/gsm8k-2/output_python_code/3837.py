def solution():
    """Kim orders a $10 meal and a drink for 2.5. She gives a 20% tip. She pays with a $20 bill. How much does she get in change?"""
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